# Guia para configurar NVIDIA Jetson Nano 2GB
Conjunto de pasos y repositorios en la Jetson Nano 2GB utilizados para el desarrollo del proyecto Dagger.
# Tabla de contenidos
- [Requerimientos](#Requerimientos)
- Guía para  instalar y configurar la tarjeta gráfica integrada NVIDIA (GPU) en el PC con Ubuntu (fuera del contenedor Docker)
- [Configuración inicial](#Configuración-inicial)

## Instalación del Jetpack 4.5 en la microSD de 64GB

- Imagen ISO del Jetpack 4.5 y guía detallada de NVIDIA (Descargar para Jetson Nano 2GB) ([Descargar imagen ISO](https://developer.nvidia.com/embedded/jetpack-sdk-45-archive)) ([Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)) :  

    > Nota: Verifique que docker está instalado correctamente utilizando los siguientes comandos. Debería mostrar la versión de cada programa.
    ```shell
    $ docker compose version
    $ docker version
    ```
    > Nota: Para formatear la microSD se usa
    
https://etcher.balena.io/
    > **Asegurese de configurar el grupo de docker**
    ```shell
    $ sudo groupadd docker
    $ sudo usermod -aG docker $USER
    $ newgrp docker
    $ reboot
    ```
# Guía para descargar y configurar el ventilador (fan control)** 

> Nota: Para seguir y descargar el [repositorio github](https://github.com/Pyrestone/jetson-fan-ctl) con todo lo necesario del ventilador. 

 [Container toolkit](https:/e).


- Un prerequisito importante es tener instalado el driver para la tarjeta gráfica NVIDIA con la que cuente el computador. Para esto, se sigue el paso a paso de la [guía de instalación](./NVIDIA_driver_install).

  > **Es necesario tener instalado Python 3. Así si puede verficar la versión actual:**
  ```shell
  $ python3 --version
  
  De otro modo puede instalar Python usando:
  $ sudo apt install python3-dev
  ```

```shell
# Instalar driver de CUDA
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# Nota: Es necesario verificar la distribución de Ubuntu en el PC, por defecto está en "ubuntu18.04", cambiar manualmente la distribución si es diferente por ejemplo a "ubuntu20.04" o "ubuntu22.04" dentro del archivo  usando el siguiente comando y guardando cambios: 

$ sudo nano /etc/apt/sources.list.d/nvidia-docker.list

# Una vez se realicen las verificaciones y modificaciones correspondientes de la distribución de Ubuntu seguir con los comandos:

$ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
$ sudo nvidia-ctk runtime configure --runtime=docker
$ sudo systemctl restart docker
```

# Guía para instalar drivers para tarjeta gráfica de NVIDIA del PC

> Nota: Se sigue el paso a paso de la [guía oficial](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html).

Resumen de prerequisitos:
- Verify the system has a CUDA-capable GPU. `lspci | grep -i nvidia`
- Verify the system is running a supported version of Linux [link](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
- Verify the system has build tools such as make, gcc installed. `gcc --version`
- Verify the system has correct Linux kernel headers. `uname -r`. Instalación en ubunto con `sudo apt-get install linux-headers-$(uname -r)`.

> Los comandos específicos para verificar cada item anterior se encuentra en [Pre-installation actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions).


## Instalación

Se descarga el archivo .run de la [página oficial](https://www.nvidia.com/Download/index.aspx?lang=en-us). Se selecciona la configuración para la tarjeta gráfica de su computador (`lspci | grep -i nvidia`), se copia el link de descargar y se instala con.

```shell
$ DOWNLOAD_URL=https://us.download.nvidia.com/XFree86/Linux-x86_64/525.116.04/NVIDIA-Linux-x86_64-525.116.04.run
$ DRIVER_RUN_FILE_NAME=NVIDIA-Linux-x86_64-525.116.04.run
$ wget -O NVIDIA-Linux-x86_64-525.116.04.run $DOWNLOAD_URL
$ chmod +x $DRIVER_RUN_FILE_NAME
$ sudo ./$DRIVER_RUN_FILE_NAME
```
> Si aparece el error de _NVIDIA kernel module 'nvidia-drm' appears to already be loaded in your kernel_, hay que deshabilitar la interfaz gráfica conforme [StackOverflow](https://unix.stackexchange.com/questions/440840/how-to-unload-kernel-module-nvidia-drm).

Luego de esto reiniciar el computador. Abrir nuevamente la terminal y correr `nvidia-smi`, debería mostrar la versión del driver.

> Si aparece el error de _Failed to initialize NVML: Driver/library version mismatch_ probar la solución que mencionan en este [foro](https://forums.developer.nvidia.com/t/failed-to-initialize-nvml-driver-library-version-mismatch/190421).

> Despues de reiniciar el PC y ejecutando el siguiente comando se valida que el driver de la tarjeta gráfica NVIDIA se ha instalado.

$ nvidia-smi  

## Cómo desintalar el CUDA toolkit y los drivers de NVIDIA.

Fuente de la información en [How to remove NVIDIA drivers?](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#removing-cuda-toolkit-and-driver)
To remove CUDA Toolkit:

```shell
sudo apt-get --purge remove "*cuda*" "*cublas*" "*cufft*" "*cufile*" "*curand*" \
 "*cusolver*" "*cusparse*" "*gds-tools*" "*npp*" "*nvjpeg*" "nsight*" "*nvvm*"
```

To remove NVIDIA Drivers:

```shell
sudo apt-get --purge remove "*nvidia*" "libxnvctrl*"
```

To clean up the uninstall:

```shell
sudo apt-get autoremove
```

Notas:
> Cuando se instala el CUDA toolkit o CUDA driver (distinto al NVIDIA driver), este instala el NVIDIA driver automáticamente. [link](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#new-features).

> Información acerca del instalador del driver de NVIDIA en [Readme](https://download.nvidia.com/XFree86/Linux-x86_64/450.80.02/README/)


# ¿Cómo correr el contenedor?
> Nota: Ir a la carpeta en donde se encuentra los archivos "Dockerfile" y "docker-compose"
```shell
$ cd /home/dagger/Descargas/dagger/Docker/docker ("Ruta de Ejemplo") 

docker$ docker compose up -d --build
docker$ bash startup.sh
```

> Nota: Para detener el contenedor utilize (fuera del contenedor)
```shell
$ cd /home/dagger/Descargas/dagger/Docker/docker ("Ruta de Ejemplo") 
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

