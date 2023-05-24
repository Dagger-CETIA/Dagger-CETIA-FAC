#!/bin/sh
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-12-1

wget https://download.stereolabs.com/zedsdk/4.0/cu121/ubuntu22
sudo apt install zstd
chmod +x ZED_SDK_Ubuntu22_cuda12.1_v4.0.3.zstd.run
./ZED_SDK_Ubuntu22_cuda12.1_v4.0.3.zstd.run -- silent
