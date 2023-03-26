# Author: Group 23 (Miguel, Akanksha, Dorian)
# Date: March 12th 2023
# Purpose: Showcase how to use the DataReceive.py library


# READ THIS COMMENT OR ELSE THERE WILL BE PROBLEMS

'''Make sure to check the value of bluetoothCommObject.successfullConnect
This value will tell you if you're connected or not - please build a contingency plan
in case connection is not successfully established (whether that is try again or raise some exception

Note: you only need to check if the connection was successfully established at the start as the connection persists as long as the object is alive'''
from processing_funcs import *
import keyboard
import matplotlib.pyplot as plt
import time
import DataReceive  # Name of the file containing the bluetooth serial object
print("Got here 1")

# Make the bluetooth object that will establish the connect and send back data

bluetoothCommObject = DataReceive.bluetoothTelephone()
print("Got here 2")
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


# checking if the knee has approached full extension/ i.e if the individual is done one instance of the SEBT test


input('Ready for anterior orientation SEBT test? Press Enter to Continue.')
# first stage of SEBT test (anterior)
print('Press spacebar key upon completion of the anterior direction.')
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

    # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    anterior_SEBT.append(bno)
    anterior_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the anterior direction finished. Moving on to anteromedial direction. ")
        break


input('Ready for anteromedial orientation SEBT test? Press Enter to Continue.')
# second stage of SEBT test (anteromedial)
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

    # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    anteromedial_SEBT.append(bno)
    anteromedial_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the anteromedial direction finished. Moving on to anterolateral direction. ")
        break

input('Ready for anterolateral orientation SEBT test? Press Enter to Continue.')
# third stage of SEBT test (anterolateral)
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

    # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    anterolateral_SEBT.append(bno)
    anterolateral_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the anterolateral direction finished. Moving on to lateral direction. ")
        break

input('Ready for lateral orientation SEBT test? Press Enter to Continue.')
# fourth stage of SEBT test (lateral)
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

    # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    lateral_SEBT.append(bno)
    lateral_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the lateral direction finished. Moving on to posterolateral direction. ")
        break

input('Ready for posterolateral orientation SEBT test? Press Enter to Continue.')
# fifth stage of SEBT test (posterolateral)
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

    # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    posterolateral_SEBT.append(bno)
    posterolateral_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the posterolateral direction finished. Moving on to posterior direction. ")
        break

input('Ready for posterior orientation SEBT test? Press Enter to Continue.')
# sixth stage of SEBT test (posterior)
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

    # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    posterior_SEBT.append(bno)
    posterior_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the posterior direction finished. Moving on to posteromedial direction. ")
        break


input('Ready for posteromedial orientation SEBT test? Press Enter to Continue.')
# seventh stage of SEBT test (posteriomedial)
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

   # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    posteromedial_SEBT.append(bno)
    posteromedial_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the posteromedial direction finished. Moving on to medial direction. ")
        break

input('Ready for medial orientation SEBT test? Press Enter to Continue.')
# eighth stage of SEBT test (medial)
while (1):

    # Call the get data function - it will return an array containing the load cell values and knee angle
    loadcells, bno, emg = bluetoothCommObject.getData()

    print("Raw Loadcell Values" + str(loadcells))
    # print(emg)
    print("Knee angle: " + str(bno))

    # calcluating center of mass value
    XCofM, YCofM = get_Cof_M(loadcells)

    # printing x and y values of center of mass for debugging purposes
    print('Center of Mass: (' + str(XCofM) + ',' + str(YCofM)+')')

    # adding data to arrays for later plotting
    medial_SEBT.append(bno)
    medial_CofMs.append((XCofM, YCofM))

    time.sleep(1)  # Sleep for 1 second

    if keyboard.is_pressed(' '):
        print("SEBT test in the medial direction finished. Testing Finished, please remove apparatus. ")
        break

print("SEBT testing finished. Email sent.")


# debugging purposes
