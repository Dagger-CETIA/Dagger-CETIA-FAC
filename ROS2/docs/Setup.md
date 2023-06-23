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

## ¿Cómo correr el contenedor?
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

