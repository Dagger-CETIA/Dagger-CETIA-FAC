# Guía para instalar drivers para tarjeta gráfica de NVIDIA


Se sigue el paso a paso de la [guía oficial](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html).

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