sudo rosdep init
rosdep update

#mkdir -p /zed_ws/src
#cd /zed_ws/src/
git clone --recursive https://github.com/stereolabs/zed-ros2-wrapper.git
cd ..
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release
echo source $(pwd)/install/local_setup.bash >> ~/.bashrc
source ~/.bashrc
