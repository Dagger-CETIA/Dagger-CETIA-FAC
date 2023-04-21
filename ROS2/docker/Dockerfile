FROM osrf/ros:foxy-desktop

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=foxy

SHELL [ "/bin/bash", "-c" ]
RUN apt-get update && apt-get install -y \
 curl \
 nano \
 git \
 python3-pip


RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc 

RUN \
 apt-get update && apt-get install -y \
 ros-${ROS_DISTRO}-gazebo-plugins \
 ros-${ROS_DISTRO}-joint-state-publisher

