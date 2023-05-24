# When building the image for the first time you need to restart the container
# docker restart zed2i
xhost +local:docker
docker exec -it zed2i /bin/bash

# source /opt/ros/foxy/setup.bash
