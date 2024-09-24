# {{cookiecutter.directory_name}}

## Run ROS2 container
```bash
sudo docker start $CONTAINER
sudo docker exec -it $CONTAINER /bin/bash
source /opt/ros/foxy/setup.bash
```

## Create and build package
```bash
cd ~/ros2_ws/src
bash create_ros2_pkg.sh {{cookiecutter.directory_name}}
bash build_ros2_pkg.sh {{cookiecutter.directory_name}}
```

## Run package
```bash
cd ~/ros2_ws
ros2 launch {{cookiecutter.directory_name}} {{cookiecutter.directory_name}}_node.launch.py
```