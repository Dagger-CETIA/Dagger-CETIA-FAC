# Guía para instalar y configurar la máquina en donde se corre el contenedor

Para configurar NVIDIA Container toolkit se utiliza la [guía](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#platform-requirements) de la página oficial de NVIDIA. 

Un prerequisito importante es tener instalado el driver para la tarjeta gráfica NVIDIA con la que cuente el computador. Para esto, se sigue el paso a paso de la [guía de instalación](./NVIDIA_driver_install).


Guía paso a paso para instalar el nvidia-docker-toolkit en [Container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#install-guide).


- Verificar que la tarjeta gráfica de su dispositivo esté habilitada para CUDA en [CUDA-capable devices](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-a-cuda-capable-gpu)
- Verificar que esté instalado el driver [oficial](https://www.nvidia.com/Download/driverResults.aspx/204837/en-us/) de la GPU.

```shell
# Instalar driver de CUDA
$ sudo apt-get install linux-headers-$(uname -r)

# Add the package repositories
$ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
$ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
$ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

$ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
$ sudo systemctl restart docker

```
