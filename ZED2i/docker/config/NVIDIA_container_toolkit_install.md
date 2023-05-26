# Guía para instalar y configurar la máquina en donde se corre el contenedor

Para configurar NVIDIA Container toolkit se utiliza la [guía](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#platform-requirements) de la página oficial de NVIDIA. 

Guía paso a paso para instalar el nvidia-docker-toolkit en [Container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#install-guide).


- Un prerequisito importante es tener instalado el driver para la tarjeta gráfica NVIDIA con la que cuente el computador. Para esto, se sigue el paso a paso de la [guía de instalación](./NVIDIA_driver_install).

```shell
# Instalar driver de CUDA
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

$ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
$ sudo nvidia-ctk runtime configure --runtime=docker
$ sudo systemctl restart docker

```
