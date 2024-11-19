
if [ $# -lt 1 ]; then
    echo "Usage: $0 <package_name>"
    exit 1
fi

PACKAGE_NAME=$1

# Create the package with the default ament_python template
ros2 pkg create $PACKAGE_NAME --build-type ament_python --dependencies rclpy cv_bridge
#!/bin/bash
# Add custom files or directories as needed
mkdir $PACKAGE_NAME/launch
LAUNCH_FILE_PATH=$PACKAGE_NAME/launch/$PACKAGE_NAME".launch.py"
SETUP_FILE_PATH=$PACKAGE_NAME/setup.py
MAIN_FILE_PATH=$PACKAGE_NAME/$PACKAGE_NAME/$PACKAGE_NAME".py"
RUN_FILE_PATH=$PACKAGE_NAME/run.sh

cp pkg_run.sh $RUN_FILE_PATH

cp pkg_setup.py $SETUP_FILE_PATH
sed -i s/PACKAGE_NAME_HERE/$PACKAGE_NAME/g $SETUP_FILE_PATH

cp pkg_node.py $MAIN_FILE_PATH
sed -i s/PACKAGE_NAME_HERE/$PACKAGE_NAME/g $MAIN_FILE_PATH

cp pkg_node.launch.py $LAUNCH_FILE_PATH
sed -i s/PACKAGE_NAME_HERE/$PACKAGE_NAME/g $LAUNCH_FILE_PATH
chmod +x $LAUNCH_FILE_PATH

echo "Custom ROS 2 Python package $PACKAGE_NAME created."