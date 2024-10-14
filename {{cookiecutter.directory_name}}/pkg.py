import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from message_filters import Subscriber, ApproximateTimeSynchronizer # for subscriber only

import cv2, os, pyrealsense2 as rs, numpy as np

package_name = 'PACKAGE_NAME_HERE'
#===========================================================
#=================================== Functions for publisher
#===========================================================
def convert_depth_to_uint8(depth_image):
    """
    Convert a 16-bit depth image to two 8-bit images.

    Args:
        depth_image (numpy.ndarray): 16-bit depth image.

    Returns:
        tuple: Two 8-bit images.
    """
    if depth_image.dtype != np.uint16:
        raise ValueError("Input depth image must be of type uint16")
    # Extract the lower 8 bits and the upper 8 bits
    low_byte_image = (depth_image & 0xFF).astype(np.uint8)[..., np.newaxis]
    high_byte_image = ((depth_image >> 8) & 0xFF).astype(np.uint8)[..., np.newaxis]
    return np.concatenate((low_byte_image, high_byte_image), axis=-1)

class ImageSender(Node):
    def __init__(self):
        super().__init__(f'{package_name}')
        self.color_publisher = self.create_publisher(Image, 'camera/color_image', 10)
        self.depth_publisher = self.create_publisher(Image, 'camera/depth_image', 10)
        self.bridge = CvBridge()

        if USE_CAM:
            # RealSense initialization
            self.pipeline = rs.pipeline()
            config = rs.config()
            config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
            config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
            self.pipeline.start(config)

        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        if USE_CAM:
            frames = self.pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            depth_frame = frames.get_depth_frame()
            if not color_frame or not depth_frame:
                return
            rgb = np.asanyarray(color_frame.get_data())
            depth = np.asanyarray(depth_frame.get_data())
        else:
            rgb = cv2.imread('data/test_images/rgb.png')[..., ::-1]
            depth = cv2.imread('data/test_images/depth.png', cv2.IMREAD_UNCHANGED)

        self.get_logger().info(f'Depth: shape {depth.shape}, dtype {depth.dtype.name}')
        color_msg = self.bridge.cv2_to_imgmsg(rgb, encoding='rgb8')
        depth_msg = self.bridge.cv2_to_imgmsg(convert_depth_to_uint8(depth), encoding='8UC2')

        self.color_publisher.publish(color_msg)
        self.depth_publisher.publish(depth_msg)

        self.get_logger().info('Published color and depth images')
        if RUN_ONCE:
            if USE_CAM:
                self.pipeline.stop()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    image_sender = ImageSender()
    rclpy.spin(image_sender)

    if not RUN_ONCE:
        if USE_CAM:
            image_sender.pipeline.stop()
        image_sender.destroy_node()
        rclpy.shutdown()

#===========================================================
#=================================== Functions for subscriber
#===========================================================
def combine_uint8_to_depth(low_byte_image, high_byte_image):
    """
    Combine two 8-bit images into a single 16-bit depth image.

    Args:
        low_byte_image (numpy.ndarray): 8-bit image representing the low byte.
        high_byte_image (numpy.ndarray): 8-bit image representing the high byte.

    Returns:
        numpy.ndarray: Combined 16-bit depth image.
    """
    if low_byte_image.shape != high_byte_image.shape:
        raise ValueError("Low byte image and high byte image must have the same shape")
    if low_byte_image.dtype != np.uint8 or high_byte_image.dtype != np.uint8:
        raise ValueError("Both input images must be of type uint8")

    # Combine the two 8-bit images to form a 16-bit image
    depth_image = (high_byte_image.astype(np.uint16) << 8) | low_byte_image.astype(np.uint16)

    return depth_image

class ImageProcessor(Node):
    def __init__(self):
        super().__init__(package_name)
        self.bridge = CvBridge()

        self.color_sub = Subscriber(self, Image, 'camera/color_image')
        self.depth_sub = Subscriber(self, Image, 'camera/depth_image')

        self.ts = ApproximateTimeSynchronizer([self.color_sub, self.depth_sub], queue_size=10, slop=0.1)
        self.ts.registerCallback(self.callback)

        self.output_dir = 'data/outputs/image_processor'
        os.makedirs(self.output_dir, exist_ok=True)


    def callback(self, color_msg, depth_msg):
        rgb = self.bridge.imgmsg_to_cv2(color_msg, 'rgb8')
        depth8U = self.bridge.imgmsg_to_cv2(depth_msg, '8UC2')
        depth = combine_uint8_to_depth(depth8U[...,0], depth8U[...,1])
        # cv2.imwrite(os.path.join(self.output_dir, f'{datetime.now().strftime("%Y%b%d%H%M%S")}.png'), rgb[..., ::-1])
        cv2.imwrite(os.path.join(self.output_dir, f'rgb.png'), rgb[..., ::-1])
        cv2.imwrite(os.path.join(self.output_dir, f'depth.png'), depth)
        self.get_logger().info('Received and processed synchronized color and depth images')

        self.process_image(rgb, depth)
        self.get_logger().info('Processed image')

    def process_image(self, rgb, depth):
        pass

def main(args=None):
    rclpy.init(args=args)
    image_processor = ImageProcessor()
    rclpy.spin(image_processor)
    image_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
