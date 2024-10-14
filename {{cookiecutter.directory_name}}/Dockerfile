#################### Pull nvidia docker image from dockerhub
FROM mtbui2010/ubuntu20.04:cuda.11.1-ros2

ARG SHARED_DIR=/root/shared
ARG PKG_DIR=/media/keti/workdir/projects

RUN mkdir -p $PKG_DIR
RUN mkdir -p $SHARED_DIR

RUN cd /root/ros2_ws
RUN rm -rf src
RUN ln -s $SHARED_DIR src

# install utils
RUN apt-get update
RUN apt install wget -y

#alias
RUN echo "alias edit_bashrc='nano ~/.bashrc'" >> /root/.bashrc
RUN echo "alias source_bashrc='source ~/.bashrc'" >> /root/.bashrc
RUN echo "alias piplseditable='pip list --editable'" >> /root/.bashrc

RUN echo 'launchros2pkg() {' >> /root/.bashrc
RUN echo '  ros2 launch "$@" "$@"_node.launch.py' >> /root/.bashrc
RUN echo '}' >> /root/.bashrc

RUN echo 'runros2pkg() {' >> /root/.bashrc
RUN echo '  ros2 run "$@" "$@"_node' >> /root/.bashrc
RUN echo '}' >> /root/.bashrc