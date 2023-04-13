from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()
connection_string = '192.168.43.135:14550'

# Connect to the drone using UDP
print("Connecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, baud=115200, wait_ready=True, rate= 20, heartbeat_timeout=120)
#230400 is the baudrate that you have set in the mission plannar or qgc

# parser = argparse.ArgumentParser()
# parser.add_argument('--connect', default='127.0.0.1:14550')
# args = parser.parse_args()
# connection_string = 'COM9'#'192.168.177.190'

# # Connect to the drone using LoRa module
# print("Connecting to vehicle on: %s" % connection_string)
# vehicle = connect(connection_string, baud=230400, wait_ready=False, rate= 20, heartbeat_timeout=120)
# #230400 is the baudrate that you have set in the mission plannar or qgc

# Function to arm and then takeoff to a user specified altitude
def arm_and_takeoff(aTargetAltitude):

  print("Basic pre-arm checks")
  # Don't let the user try to arm until autopilot is ready
  while not vehicle.is_armable:
    print(" Waiting for vehicle to initialise...")
    time.sleep(1)
        
  print("Arming motors")
  # Copter should arm in GUIDED mode
  vehicle.mode    = VehicleMode("GUIDED")
  print(vehicle.mode)
  #print(vehicle._autopilot_type)
  vehicle.armed   = True
  #print(" is vehicle armed?" % vehicle.armed)

  while not vehicle.armed:
    print(" Waiting for arming...")
    time.sleep(1)

  print("Taking off!")
  vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

#   # Check that vehicle has reached takeoff altitude
  while True:
     print(" Altitude: ", vehicle.location.global_relative_frame.alt, "mts") 
     #Break and return from function just below target altitude.        
     if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
       print("Reached target altitude")
       break
     time.sleep(1)

## Test motors speed in m/s
#vehicle.airspeed = 1

# # # Initialize the takeoff sequence in meters
arm_and_takeoff(1.5)

print("Take off complete")

# # # Hover for 10 seconds
time.sleep(2)

#print("Now let's land")
print("Landing...")
vehicle.mode = VehicleMode("LAND")

# Close vehicle object
vehicle.close()
