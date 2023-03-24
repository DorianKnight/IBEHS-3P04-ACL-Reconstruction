# Author: Group 23 (Miguel, Akanksha, Dorian)
# Date: March 12th 2023
# Purpose: Showcase how to use the DataReceive.py library


# READ THIS COMMENT OR ELSE THERE WILL BE PROBLEMS

'''Make sure to check the value of bluetoothCommObject.successfullConnect
This value will tell you if you're connected or not - please build a contingency plan
in case connection is not successfully established (whether that is try again or raise some exception

Note: you only need to check if the connection was successfully established at the start as the connection persists as long as the object is alive'''

import DataReceive  # Name of the file containing the bluetooth serial object
import time

# Make the bluetooth object that will establish the connect and send back data
bluetoothCommObject = DataReceive.bluetoothTelephone()
if (bluetoothCommObject.successfullConnect == True):
    print("Connection was successfully established \n")
else:
    print("Connection was not successfully established")

# important constants stated here
x1, y1 = -4.1, 5.85
x2, y2 = 4.1, 5.85
x3, y3 = -4.1, -5.85
x4, y4 = 4.1, -5.85


# arrays for holding angle data from each direction of the SEBT test
anterior_SEBT = []
anterolateral_SEBT = []
anteromedial_SEBT = []
lateral_SEBT = []
medial_SEBT = []
posterolateral_SEBT = []
posteromedial_SEBT = []
posterior_SEBT = []

# arrays for holding foot center of mass data during each direction of the SEBT test
anterior_CofMs = []
anterolateral_CofMs = []
anteromedial_CofMs = []
lateral_CofMs = []
medial_CofMs = []
posterolateral_CofMs = []
posteromedial_CofMs = []
posterior_CofMs = []

calibration_value = 0

# checking if the knee has approached full extension/ i.e if the inndividual is done one instance of the SEBT test


def is_knee_extended(angle):
    if angle >= calibration_value + 2:
        return True
    return False


while (1):

    # Call the get data function - it will return an array containing the load cell values and separately it will return the knee angle and the EMG raw signal
    loadcells, bno, emg = bluetoothCommObject.getData()

    print(loadcells)
    print(bno)
    print(emg)

    # calculating the center of mass value (x value) of the 4 loadcells and returning that value
    XCofM = (loadcells[1]*x1 + loadcells[1]*x2 +
             loadcells[3]*x3 + loadcells[4]*x4)/sum(loadcells)

    # calculating the center of mass value (y value) of the 4 loadcells and returning that value
    YCofM = (loadcells[1]*y1 + loadcells[1]*y2 +
             loadcells[3]*y3 + loadcells[4]*y4)/sum(loadcells)

    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # You must repeatidly call the getData() method to get new data, it won't run in the background and automatically refresh your values
    # You ran call the getData() function at a maximum rate of 1 call every 150 ms

    # If you do run this code faster than 150 ms, the sock.recv() function will wait until there's new data to be received which is only put onto the socket every 150 ms so in fact we're hard limited to a max sampling rate of once every 150 ms.
    # This rate could be improved but only by altering the arduino code - talk to Dorian Knight if this is an issue
    time.sleep(1)  # Sleep for 1 second
