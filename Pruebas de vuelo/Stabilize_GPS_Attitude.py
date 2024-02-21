import asyncio
import mavsdk
import threading
import sys
import serial.tools.list_ports
from mavsdk.offboard import (OffboardError, PositionNedYaw)

# Variable global para rastrear si se debe aterrizar el dron
land_drone = False

# Función para aterrizar el dron
async def land_drone_function(drone):
    global land_drone
    await asyncio.sleep(1)  # Da tiempo para que se establezca la conexión con el dron

    # Bucle principal de control
    while True:
        if land_drone:
            print("Aterrizando el dron...")
            await drone.action.land()
            break
        await asyncio.sleep(0.1)  # Frecuencia del bucle de control
        break

# Función para manejar las teclas presionadas
def on_key_press():
    global land_drone
    while True:
        key = input("Presiona 'l' para aterrizar el dron o 'q' para salir: ")
        if key.lower() == 'l':
            print("Tecla 'l' presionada.")
            land_drone = True
        elif key.lower() == 'q':
            print("Tecla 'q' presionada. Saliendo...")
            sys.exit()
        else:
            print(f"Tecla '{key}' no reconocida.")

# Conectar al dron y ejecutar el código de estabilización
async def position_hold(drone):
    await drone.action.set_takeoff_altitude(1.5)  # Configura la altitud de despegue en 1.5 metros
    print("Altura de TakeOff configurada a 1.5 metros")
    await drone.action.arm()
    await drone.action.takeoff()

    # Bucle principal de control
    while True:
        try:
            # Obtén la posición actual del dron
            async for position in drone.telemetry.position():
                # Recupera los datos de latitud, longitud y altitud
                latitud = position.latitude_deg
                longitud = position.longitude_deg
                altitud = position.relative_altitude_m

                # Calcula el error con respecto a la posición deseada (ajustar según sea necesario)
                error_x = 0.0 - latitud
                error_y = 0.0 - longitud
                error_z = 1.5 - altitud

                # Ajusta la actitud del dron en función del error
                await drone.offboard.set_position_ned(PositionNedYaw(error_x, error_y, error_z, 0.0))

                # Imprime la posición actual
                print("Posición:", position)
                break  # Sal de este bucle después de obtener la posición una vez

        except Exception as e:
            print(f"Error al obtener la posición: {e}")

        await asyncio.sleep(0.1)  # Frecuencia del bucle de control

        await land_drone_function(drone)

        if land_drone == True:
            break


# Conectar al dron y ejecutar el código
async def run():
    drone = mavsdk.System()

    # Listado de puertos ttyACM disponibles
    puertos_disponibles = serial.tools.list_ports.comports() 
    puertos_ttyACM = [puerto.device for puerto in puertos_disponibles if "ttyACM" in puerto.device]
    
    if puertos_ttyACM:
        print("Puertos ttyACM disponibles:")
        for port_ttyACM in puertos_ttyACM:
            print(port_ttyACM)
    else:
        print("No se encontraron puertos ttyACM disponibles.")
                                                                                               
    # Conexión al primer puerto ttyACM encontrado
    await drone.connect(system_address="serial://" + port_ttyACM + ":57600")
    #await drone.connect(system_address="udp://:14540")

    # Iniciar un hilo separado para capturar las teclas presionadas
    key_thread = threading.Thread(target=on_key_press)
    key_thread.daemon = True
    key_thread.start()

    # Ejecutar la función para mantener la posición del dron
    await position_hold(drone)

    # Ejecutar la función para aterrizar el dron

# Crear un bucle de eventos y ejecutar el código
if _name_ == "_main_":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
