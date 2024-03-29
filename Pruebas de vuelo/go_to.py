"""
© Copyright 2015-2016, 3D Robotics.
simple_goto.py: GUIDED mode "simple goto" example (Copter Only)

Demonstrates how to arm and takeoff in Copter and how to navigate to points using Vehicle.simple_goto.

Full documentation is provided at http://python.dronekit.io/examples/simple_goto.html
"""

from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()
connection_string = '192.168.43.135:14550'

# Connect to the drone using UDP
print("Connecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, baud=115200, wait_ready=True, rate= 20, heartbeat_timeout=120)
#115200 is the baudrate that you have set in the mission plannar or qgc

# Connect to the drone usind LoRa module
#print("Connecting to vehicle on: %s" % connection_string)
#vehicle = connect(connection_string, baud=230400, wait_ready=True, heartbeat_timeout=120)
#230400 is the baudrate that you have set in the mission plannar or qgc

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Drone should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    #   Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt, "mts")
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Initialize the takeoff sequence in meters
arm_and_takeoff(2)

# Speed in m/s
print("Set drone speed to 3.6 km/h")
vehicle.airspeed = 1

# Set point 1 (Latitude, Longitude, "Altitude in meters (relative to the home location")
print("Going towards first point...")
#point1 = LocationGlobalRelative(4.725515809464003, -74.27058715248589, 2)
point1 = LocationGlobalRelative(4.726663, -74.270183, 2)
vehicle.simple_goto(point1)

# Sleep so we can see the change in map
time.sleep(10)

# Set groundspeed in m/s
vehicle.simple_goto(point1, groundspeed = 1)

# sleep so we can see the change in map
time.sleep(10)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

# Close vehicle object before exiting script
vehicle.close()
