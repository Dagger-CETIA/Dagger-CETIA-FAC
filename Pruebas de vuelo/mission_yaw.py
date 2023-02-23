#!/usr/bin/env python
## https://www.elucidatedrones.com/posts/drone-flying-in-square-path-using-dronekit-python/
#..................................................................................

# Import Necessary Packages
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time, math
import argparse  
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()
connection_string = 'COM9'#'192.168.177.190'

def basic_takeoff(altitude):

    """

    This function take-off the vehicle from the ground to the desired
    altitude by using dronekit's simple_takeoff() function.

    Inputs:
        1.  altitude            -   TakeOff Altitude

    """

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    time.sleep(2)
    vehicle.simple_takeoff(altitude)

    while True:
        print("Reached Height = ", vehicle.location.global_relative_frame.alt)

        if vehicle.location.global_relative_frame.alt >= (altitude - 1.5):
            break

def change_mode(mode):

    """

    This function will change the mode of the Vehicle.

    Inputs:
        1.  mode            -   Vehicle's Mode

    """

    vehicle.mode = VehicleMode(mode)

def send_to(latitude, longitude, altitude):

    """

    This function will send the drone to desired location, when the 
    vehicle is in GUIDED mode.

    Inputs:
        1.  latitude            -   Destination location's Latitude
        2.  longitude           -   Destination location's Longitude
        3.  altitude            -   Vehicle's flight Altitude

    """

    if vehicle.mode.name == "GUIDED":
        location = LocationGlobalRelative(latitude, longitude, float(altitude))
        vehicle.simple_goto(location)
        time.sleep(1)

def distance_calculation(homeLattitude, homeLongitude, destinationLattitude, destinationLongitude):

    """

    This function returns the distance between two geographiclocations using
    the haversine formula.

    Inputs:
        1.  homeLattitude          -   Home or Current Location's  Latitude
        2.  homeLongitude          -   Home or Current Location's  Longitude
        3.  destinationLattitude   -   Destination Location's  Latitude
        4.  destinationLongitude   -   Destination Location's  Longitude

    """

    # Radius of earth in metres
    R = 6371e3

    rlat1, rlon1 = homeLattitude * (math.pi/180), homeLongitude * (math.pi/180)
    rlat2, rlon2 = destinationLattitude * (math.pi/180), destinationLongitude * (math.pi/180)
    dlat = (destinationLattitude - homeLattitude) * (math.pi/180)
    dlon = (destinationLongitude - homeLongitude) * (math.pi/180)

    # Haversine formula to find distance
    a = (math.sin(dlat/2) * math.sin(dlat/2)) + (math.cos(rlat1) * math.cos(rlat2) * (math.sin(dlon/2) * math.sin(dlon/2)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # Distance (in meters)
    distance = R * c

    return distance

def destination_location(homeLattitude, homeLongitude, distance, bearing):

    """

    This function returns the latitude and longitude of the
    destination location, when distance and bearing is provided.

    Inputs:
        1.  homeLattitude       -   Home or Current Location's  Latitude
        2.  homeLongitude       -   Home or Current Location's  Longitude
        3.  distance            -   Distance from the home location
        4.  bearing             -   Bearing angle from the home location

    """

    # Radius of earth in metres
    R = 6371e3

    rlat1, rlon1 = homeLattitude * (math.pi/180), homeLongitude * (math.pi/180)

    d = distance

    #Converting bearing to radians
    bearing = bearing * (math.pi/180)

    rlat2 = math.asin((math.sin(rlat1) * math.cos(d/R)) + (math.cos(rlat1) * math.sin(d/R) * math.cos(bearing)))
    rlon2 = rlon1 + math.atan2((math.sin(bearing) * math.sin(d/R) * math.cos(rlat1)) , (math.cos(d/R) - (math.sin(rlat1) * math.sin(rlat2))))

    #Converting to degrees
    rlat2 = rlat2 * (180/math.pi) 
    rlon2 = rlon2 * (180/math.pi)

    # Lat and Long as an Array
    location = [rlat2, rlon2]

    return location

def square_calculation(side_length):

    """

    This function will generate the geographical coordinates (latitudes & longitudes)
    of the square path with the given side length. The origin or reference location
    for the generation of the square trajectory is the vehicle's current location.

    Inputs:
        1.  side_length         -   Side length of the square

    """

    # Vehicle's heading and current location
    angle          =  int(vehicle.heading)
    loc            =  (vehicle.location.global_frame.lat, vehicle.location.global_frame.lon, vehicle.location.global_relative_frame.alt)

    # Declaring a array variable to store
    # the geogrpahical location of square points
    final_location =  []

    for count in range(4):
        new_loc =  destination_location(homeLattitude = loc[0], homeLongitude = loc[1], distance = side_length, bearing = angle)
        final_location.append((new_loc[0], new_loc[1], loc[2]))
        loc     =  (new_loc[0], new_loc[1], loc[2])

        # Incrementing heading angle
        angle  +=  90

    return final_location

def square_mission(side_length):

    """

    This function retrieves the square coordinates from the square_calculation()
    function and guides the vehicle to the retrieved points.

    Inputs:
        1.  side_length         -   Side length of the square

    """

    # Retrieving the array of the locations of the square path
    locations  =  square_calculation(side_length = side_length)

    for location in locations:

        # Send vehicle to the destination
        send_to(latitude = location[0], longitude = location[1], altitude = location[2])

        while True:

            # Distance between the current location of the vehicle and the destination
            distance = distance_calculation(homeLattitude = vehicle.location.global_frame.lat,
                                            homeLongitude = vehicle.location.global_frame.lon,
                                            destinationLattitude  = location[0],
                                            destinationLongitude = location[1])

            if distance <= 1.8:
                break

            time.sleep(2)

def main():

    # Declaring Vehicle as global variable
    global vehicle
    import argparse 
    connection_string = 'COM9'#'192.168.177.190'

    print("Connecting to vehicle on: %s" % connection_string)
    vehicle = connect(connection_string, baud=230400, wait_ready=True, rate= 20, heartbeat_timeout=120)
    #230400 is the baudrate that you have set in the mission plannar or qgc

    # Setting the Heading angle constant throughout flight
    if vehicle.parameters['WP_YAW_BEHAVIOR'] != 0:
        vehicle.parameters['WP_YAW_BEHAVIOR'] = 0
        print("Changed the Vehicle's WP_YAW_BEHAVIOR parameter")

    # # # Initialize the takeoff sequence in meters
    # basic_takeoff(2)

    # print("Take off complete")

    # # # # Hover in seconds
    # time.sleep(2)

    # side = 2
    # square_mission(side_length = side)

    # time.sleep(2)

    # #print("Now let's land")
    # print("Landing...")
    # change_mode = VehicleMode("LAND")


    while True:

        # Getting Input from User
        value = input("Enter your Input:\n").upper()

        if value == 'TAKEOFF':
            basic_takeoff(altitude = 2)

        if value == 'LAND':
            change_mode(mode = value)

        if value == 'SQUARE':
            side = int(input("Enter Side Length of the Square Path (in meters):\n"))
            square_mission(side_length = side)

if __name__ == "__main__":
    main()