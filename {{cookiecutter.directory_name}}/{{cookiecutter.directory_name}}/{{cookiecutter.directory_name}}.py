import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
import os
package_name = os.path.basename(os.path.dirname(__file__))

class ImageSender(Node):
    def __init__(self):
        super().__init__(f'{package_name}')
        # self.publisher = self.create_publisher(Image, 'camera/color_image', 10)
        # self.bridge = CvBridge()
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        # self.get_logger().info(f'Depth: shape {depth.shape}, dtype {depth.dtype.name}')
        # color_msg = self.bridge.cv2_to_imgmsg(rgb, encoding='rgb8')
        # self.color_publisher.publish(color_msg)
        self.get_logger().info('Published color and depth images')

def main(args=None):
    rclpy.init(args=args)
    image_sender = ImageSender()
    rclpy.spin(image_sender)


if __name__ == '__main__':
    main()
