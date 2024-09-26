#################### Pull nvidia docker image from dockerhub
FROM mtbui2010/ubuntu20.04:cuda.11.1-ros2

ARG SHARED_DIR=/root/shared
ARG PKG_DIR=/media/keti/workdir/projects

RUN mkdir -p $PKG_DIR
RUN mkdir -p $SHARED_DIR

RUN cd /root/ros2_ws
RUN rm -rf src
RUN ln -s $SHARED_DIR src