# Guia para configurar NVIDIA Jetson Nano 2GB
Conjunto de pasos y repositorios utilizados para el desarrollo del proyecto Dagger usando la ([NVIDIA Jetson Nano Developer Kit 2GB.](https://developer.nvidia.com/embedded/learn/jetson-nano-2gb-devkit-user-guide))  

# Tabla de contenidos
- [Requerimientos](#Requerimientos)
- Instalación de Jetpack 4.6.1 (con Ubuntu 18.04) en la microSD de 64GB
- [Configuración inicial](#Configuración-inicial)

## Instalación de Jetpack 4.6.1 (con Ubuntu 18.04)

- Seguir los pasos:
  
    1- Descargar imagen Jetpack 4.6.1 y guía con más detalles ([Descargar imagen ISO](https://developer.nvidia.com/embedded/jetpack-sdk-461)) 

    2- Formatear la micro SD usando ([SD Card Formatter](https://www.sdcard.org/downloads/formatter/)) en Windows/Mac o en Linux seguir los ([pasos](https://www.softzone.es/linux/tutoriales/formatear-linux/))

    3- Flashear la imagen Jetpack descargada en el paso 1 en la microSD usando ([balena](https://etcher.balena.io/)) disponibles para Windows/Linux/Mac.

    4- Insertar la microSD en la ranura de la NVIDA Jetson. Realizar las configuraciones y actulizaciones correspondientes con: 
  
    ```shell
    $ sudo apt-get update
    $ sudo apt-get upgrade
    ```

## Guía para activar el ventilador (fan control) 

- Se siguen los pasos del [repositorio github](https://github.com/Pyrestone/jetson-fan-ctl) con todo lo necesario del ventilador.

> #### NOTA: Se puede descargar el script de Python [jetsonFanControl.py](https://github.com/Dagger-CETIA/Dagger-CETIA-FAC/blob/main/jetsonFanControl.py) y ejecutarlo directamente con el siguiente comando.

  ```shell
  $ sudo python3 jetsonFanControl.py
   ```   


  1- Es necesario tener instalado Python 3. Así si puede verficar la versión actual:

  ```shell
  $ python3 --version
  
  > De otro modo se puede instalar Python usando:
  
  $ sudo apt install python3-dev
    ```
  2- Clonar el repositorio usando: 

  ```shell
  $ git clone https://github.com/Pyrestone/jetson-fan-ctl.git
   ```    
  3- Dentro de la carpeta clonada (jetson-fan-ctl) ejecutar:
  ```shell
  $ sudo ./install.sh
   ```

  ## Guía para configurar y hacer la conexión serial entre la NVIDA Jetson Nano y la Pixhawk 2.4.8

> Se siguen los pasos del [foro](https://www.hackster.io/Matchstic/connecting-pixhawk-to-raspberry-pi-and-nvidia-jetson-b263a7). 

  1- Actulizaciones:

  ```shell
  $ sudo apt-get update
    ```

  2- Instalar pip para Python 

  ```shell
  $ sudo apt-get install python3-pip
  $ sudo apt install python-pip
   ```

  3- Instalar todas las dependencias para MAVProxy:
  
  ```shell
  $ sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-matplotlib python3-lxml libxml2-dev libxslt-dev
  $ sudo mavproxy.py --master=/dev/ttyTHS1
  - Para la Raspberry Pi 4 modelo B:
  $ sudo mavproxy.py --master=/dev/ttyACM0
   ```

  ## Guía para descargar y configurar el reconocimiento de Objetos

> Se siguen los pasos del [repositorio](https://github.com/dusty-nv/jetson-inference). 

  1- Actulizaciones:

  ```shell
  $ sudo apt-get update
    ```

  2- Clonar el repositorio jetson-inference usando:

  ```shell
  $ git clone --recursive https://github.com/dusty-nv/jetson-inference  
   ```

  3- Dentro del directorio clonado (jetson-inference) correr el contenedor de Docker:
  
  ```shell
  $ cd jetson-inference
  $ docker/run.sh
   ```
  4- Para correr el modelo de Detección de Objetos :
  
  ```shell
  $ cd jetson-inference
  $ docker/run.sh
   ``` 
