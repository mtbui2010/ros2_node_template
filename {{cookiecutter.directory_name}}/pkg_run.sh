NODE_NAME={{cookiecutter.directory_name}}
source /opt/ros/foxy/setup.bash
source ~/ros2_ws/install/setup.bash
cd $ROSWS
$ROSPY $NODE_NAME/$NODE_NAME/$NODE_NAME.py