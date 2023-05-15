ARG UBUNTU_VERSION=22.04
ARG CUDA_VERSION=11.5
ARG ZED_SDK_VERSION=4.5.1

FROM nvidia/cuda:${CUDA_VERSION}-devel-ubuntu${UBUNTU_VERSION}

ENV TZ=America/Los_Angeles
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download and install CUDA
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb \
    && sudo dpkg -i cuda-keyring_1.0-1_all.deb \
    && rm cuda-keyring_1.0-1_all.deb \
    && sudo apt-get update \
    && sudo apt-get -y install cuda

# Install ZED SDK
RUN wget -q -O ZED_SDK_Linux_Ubuntu${UBUNTU_VERSION}.run \
    https://download.stereolabs.com/zedsdk/${ZED_SDK_VERSION}/ubuntu${UBUNTU_VERSION}/cuda${CUDA_VERSION}/zed_sdk_${ZED_SDK_VERSION}cuda${CUDA_VERSION}_ubuntu${UBUNTU_VERSION}.run \
    && chmod +x ZED_SDK_Linux_Ubuntu${UBUNTU_VERSION}.run \
    && ./ZED_SDK_Linux_Ubuntu${UBUNTU_VERSION}.run silent \
    && rm ZED_SDK_Linux_Ubuntu${UBUNTU_VERSION}.run

# Install ROS Humble
ENV ROS_DISTRO humble
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*
RUN sh -c 'echo "deb [trusted=yes] http://packages.ros.org/ros/ubuntu jammy main" > /etc/apt/sources.list.d/ros2.list'
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-${ROS_DISTRO}-desktop \
    && rm -rf /var/lib/apt/lists/*

# Install other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# Bootstrap rosdep
RUN rosdep init && rosdep update

# Create workspace
ENV ROS_WS /ros_ws
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS

# Clone source
RUN cd src && \
    wget -O ros2.repos https://raw.githubusercontent.com/ros2/ros2/main/ros2.repos && \
    vcs import ./ < ros2.repos

# Install dependencies
RUN apt-get update && rosdep install --from-paths src --ignore-src -r -y && rm -rf /var/lib/apt/lists/*

# Build
RUN colcon build --symlink-install --packages-select rviz2

# Set entrypoint
COPY ros_entrypoint.sh /
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]

