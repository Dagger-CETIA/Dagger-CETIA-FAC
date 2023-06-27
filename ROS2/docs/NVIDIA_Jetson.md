# Guia para configurar NVIDIA Jetson Nano 2GB
Conjunto de pasos y repositorios utilizados para el desarrollo del proyecto Dagger usando la ([NVIDIA Jetson Nano Developer Kit 2GB.](https://developer.nvidia.com/embedded/learn/jetson-nano-2gb-devkit-user-guide))  

# Tabla de contenidos
- [Requerimientos](#Requerimientos)
- Instalación de Jetpack 4.5 (con Ubuntu 18.04) en la microSD de 64GB
- [Configuración inicial](#Configuración-inicial)

## Instalación de Jetpack 4.5 (con Ubuntu 18.04) en microSD de 64GB

- Seguir los pasos a continuación:
  
    1- Descargar imagen Jetpack 4.5 y guía con más detalles ([Descargar imagen ISO](https://developer.nvidia.com/embedded/jetpack-sdk-45-archive)) 

    2- Formatear la micro SD usando ([SD Card Formatter](https://www.sdcard.org/downloads/formatter/)) en Windows/Mac o en Linux seguir los ([pasos](https://www.softzone.es/linux/tutoriales/formatear-linux/))

    3- Flashear la imagen Jetpack descargada en el paso 1 en la microSD usando ([balena](https://etcher.balena.io/)) disponibles para Windows/Linux/Mac.

    4- Insertar la microSD en la ranura de la NVIDA Jetson. Realizar las configuraciones y actulizaciones correspondientes con: 
  
    ```shell
    $ sudo apt-get update
    $ sudo apt-get upgrade
    ```

## Guía para activar el ventilador (fan control) 

- Se siguen los pasos del [repositorio github](https://github.com/Pyrestone/jetson-fan-ctl) con todo lo necesario del ventilador. 

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

  ## Guía para configurar y hacer la conexión serial entre la NVIDA Jetson Nano y la Pixhawk 2.4.8 el ventilador (fan control) 

- Se siguen los pasos del [repositorio github](https://github.com/Pyrestone/jetson-fan-ctl) con todo lo necesario del ventilador. 

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
