# Proyecto Dagger
Conjunto de paquetes de ROS2 utilizados para el desarrollo del proyecto Dagger.
# Tabla de contenidos
- [Requerimientos](#Requerimientos)
- [¿Cómo correr el contenedor?](#Cómo-correr-el-contenedor)
- [Configuración inicial](#Configuración-inicial)

## Requerimientos

- Docker y docker compose - ¿Cómo instalar? ([Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)) ([Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)) :  

    > Nota: Verifique que docker está instalado correctamente utilizando los siguientes comandos. Debería mostrar la versión de cada programa.
    ```shell
    $ docker compose version
    $ docker version
    ```

    > **Asegurese de configurar el grupo de docker**
    ```shell
    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER
    $ newgrp docker
    $ reboot
    ```
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




# ¿Cómo correr el contenedor?
```shell
$ cd dagger_ws/docker
docker$ docker compose up -d --build
docker$ bash startup.sh
```

> Nota: Para detener el contenedor utilize (fuera del contenedor)
```shell
$ cd dagger_ws/docker
docker$ docker compose down -v
``` 

## Configuración inicial
Una vez con el contenedor en ejecución, dentro de este:

- Construya el *workspace* con
    ```shell
    dagger_ws$ colcon build
    ```
    Esto genera los nuevos directorios **build**, **install**, **log** con las dependencias de los paquetes que utiliza el *workspace*.

- Cargue las variables de entorno del *workspace* con el comando

    ```shell
    $ source dagger_ws/install/setup.bash
    ```
    > Nota: Este comando debe ejecutarse **cada vez** que ingresa al contenedor

