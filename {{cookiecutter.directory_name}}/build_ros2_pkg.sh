if [ $# -lt 1 ]; then
    echo "Usage: $0 <package_name>"
    exit 1
fi

PACKAGE_NAME=$1

cd ~/ros2_ws
colcon build --packages-select $PACKAGE_NAME
source ~/ros2_ws/install/setup.bash

echo "Custom ROS 2 Python package $PACKAGE_NAME built."