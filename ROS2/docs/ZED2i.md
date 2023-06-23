## CÁMARA Stereolabs ZED2i

> Información acerca del [repositorio "zed-ros-wrapper"](https://github.com/stereolabs/zed-ros-wrapper/) de la Cámara Stereolabs ZED - ROS 

**Es necesario estar dentro del contenedor docker para clonar el repositorio "zed-ros-wrapper"**

> Comandos para correr el contenedor:

```shell
$ cd /home/dagger/Descargas/dagger/Docker/docker ("Ruta de Ejemplo") 

docker$ docker compose up -d --build
docker$ bash startup.sh
```

Una vez dentro del contenedor docker crear la carpeta "src" dentro del workspace "zed_ws" y ejecutar:
```shell
$ sudo rosdep init
$ rosdep update

$ mkdir -p /zed_ws/src
$ cd /zed_ws/src/
$ git clone --recursive https://github.com/stereolabs/zed-ros2-wrapper.git
$ cd ..
$ rosdep install --from-paths src --ignore-src -r -y
$ colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release
$ echo source $(pwd)/install/local_setup.bash >> ~/.bashrc
$ source ~/.bashrc

```

**Ejecutar ZED wrapper**

$ roslaunch zed_wrapper zed2i.launch
