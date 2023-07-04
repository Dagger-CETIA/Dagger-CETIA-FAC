import os
import subprocess

# Ruta de la carpeta Descargas
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Clonar el repositorio en la carpeta Descargas
repo_url = "https://github.com/Pyrestone/jetson-fan-ctl.git"
repo_path = os.path.join(downloads_path, "jetson-fan-ctl")

subprocess.run(["git", "clone", repo_url, repo_path])

# Cambiar al directorio del repositorio
os.chdir(repo_path)

# Instalar las dependencias
subprocess.run(["sudo", "apt-get", "update"])
subprocess.run(["sudo", "apt-get", "install", "build-essential", "libi2c-dev", "i2c-tools"])

# Compilar el programa
subprocess.run(["make"])

# Instalar el programa
subprocess.run(["sudo", "make", "install"])

# Reiniciar el sistema para aplicar los cambios
subprocess.run(["sudo", "reboot"])
