#!/bin/bash
if [ $# -lt 2 ]; then
    echo "Usage: $0 <container_name> <version>"
    exit 1
fi
CONTAINER=$1
IMAGE=mtbui2010/$1:$2

sudo docker exec $CONTAINER rm -rf /root/ros2_ws/src
echo ========== copying packages
sudo docker exec $CONTAINER cp -rL /root/shared /root/ros2_ws/src
echo ========== copy completed.

echo ========== commiting image $IMAGE
sudo docker commit $CONTAINER $IMAGE
echo ========== image $IMAGE commited.

sudo docker exec $CONTAINER rm -rf /root/ros2_ws/src
sudo docker exec $CONTAINER ln -s /root/shared /root/ros2_ws/src
