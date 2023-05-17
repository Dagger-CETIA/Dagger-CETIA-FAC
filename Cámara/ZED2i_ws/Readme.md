Start a Docker Container on NVIDIA Jetson Nano#
docker run --gpus all -it --privileged stereolabs/zed:3.8-tools-devel-l4t-r32.7

Start a Docker Container on the NVIDIA Jetson Nano with ZED GUI
xhost +si:localuser:root  # allow containers to communicate with X server
docker run -it --runtime nvidia --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix stereolabs/zed:3.8-tools-devel-l4t-r32.7

Install ROS Noetic on NVIDIA Jetson Nano
https://www.waveshare.com/wiki/Install_ROS_System_on_Jetson_Nano_%26_Environment_Cofiguration
