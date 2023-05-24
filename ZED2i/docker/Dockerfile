FROM ubuntu:22.04

## Installs ROS2 humble with gazebo garden
# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=humble

SHELL [ "/bin/bash", "-c" ]

# Useful general packages
RUN apt-get update && apt-get install -y \
    nano \
    python3-pip \
    sudo

# Helpful packages for ROS development
RUN pip3 install -U empy pyros-genmsg setuptools

#ROS2 installation
RUN apt install -y software-properties-common
RUN add-apt-repository universe
RUN apt update && apt install curl -y
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN apt update
RUN apt install -y ros-${ROS_DISTRO}-desktop python3-argcomplete
RUN apt install -y ros-dev-tools
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc 

# Gazebo installation
RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null \
    && apt-get update \
    && apt-get install -y gz-garden


# Setup the ZED SDK
RUN DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration
RUN sudo apt install zstd
RUN wget -O ZED_SDK_Ubuntu22_cuda12.1_v4.0.3.zstd.run https://download.stereolabs.com/zedsdk/4.0/cu121/ubuntu22 \
    && chmod +x ZED_SDK_Ubuntu22_cuda12.1_v4.0.3.zstd.run && DEBIAN_FRONTEND=noninteractive ./ZED_SDK_Ubuntu22_cuda12.1_v4.0.3.zstd.run -- silent runtime_only

CMD ["/bin/bash"]
