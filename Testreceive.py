# Author: Group 23 (Miguel, Akanksha, Dorian)
# Date: March 12th 2023
# Purpose: Showcase how to use the DataReceive.py library


import DataReceive  # Name of the file containing the bluetooth serial object
import time
import matplotlib.pyplot as plt
import keyboard
from email_setup import *
from processing_funcs import *
from plotting import *
from os import listdir
from os.path import isfile, join


# setting clinician email
clinician_email = 'nehetea@mcmaster.ca'

# READ THIS COMMENT OR ELSE THERE WILL BE PROBLEMS

'''Make sure to check the value of bluetoothCommObject.successfullConnect
This value will tell you if you're connected or not - please build a contingency plan
in case connection is not successfully established (whether that is try again or raise some exception

Note: you only need to check if the connection was successfully established at the start as the connection persists as long as the object is alive'''

# Make the bluetooth object that will establish the connect and send back data

bluetoothCommObject = DataReceive.bluetoothTelephone()
if (bluetoothCommObject.successfullConnect == True):
    print("Connection was successfully established \n")
else:
    print("Connection was not successfully established")


# initializing arrays for holding angle data from each direction of the SEBT test for nonoperative leg
anterior_SEBT_nonop = []
anterolateral_SEBT_nonop = []
anteromedial_SEBT_nonop = []
lateral_SEBT_nonop = []
medial_SEBT_nonop = []
posterolateral_SEBT_nonop = []
posteromedial_SEBT_nonop = []
posterior_SEBT_nonop = []

# initializing arrays for holding angle data from each direction of the SEBT test for operative leg
anterior_SEBT_op = []
anterolateral_SEBT_op = []
anteromedial_SEBT_op = []
lateral_SEBT_op = []
medial_SEBT_op = []
posterolateral_SEBT_op = []
posteromedial_SEBT_op = []
posterior_SEBT_op = []


# arrays for holding foot center of mass data during each direction of the SEBT test for nonoperative leg
anterior_CofMs_nonop = []
anterolateral_CofMs_nonop = []
anteromedial_CofMs_nonop = []
lateral_CofMs_nonop = []
medial_CofMs_nonop = []
posterolateral_CofMs_nonop = []
posteromedial_CofMs_nonop = []
posterior_CofMs_nonop = []

# arrays for holding foot center of mass data during each direction of the SEBT test for operative leg
anterior_CofMs_op = []
anterolateral_CofMs_op = []
anteromedial_CofMs_op = []
lateral_CofMs_op = []
medial_CofMs_op = []
posterolateral_CofMs_op = []
posteromedial_CofMs_op = []
posterior_CofMs_op = []


# function for conducting each stage of the SEBT test
def conduct_stage(stage_array: list[float], leg: str, CofM_array: list[tuple], stage_name: str):
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
        stage_array.append(bno)
        CofM_array.append((XCofM, YCofM))

        time.sleep(0.150)  # Sleep for 1 second

        if keyboard.is_pressed(' '):
            print(
                f"SEBT test in the {stage_name} direction finished on the {leg} leg.")
            break


# first stage of SEBT test (anterior) on non-operative leg
input('Ready for anterior orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the anterior direction.')
conduct_stage(anterior_SEBT_nonop, 'non-operative',
              anterior_CofMs_nonop, 'anterior')
print("Moving on to the anteromedial direction of the test.")


# first stage of SEBT test (anteromedial) on non-operative leg
input('Ready for anteromedial orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the anteromedial direction.')
conduct_stage(anteromedial_SEBT_nonop, 'non-operative',
              anteromedial_CofMs_nonop, 'anteromedial')
print("Moving on to the anterolateral direction of the test.")


# third stage of SEBT test (anterolateral) on non-operative leg
input('Ready for anterolateral orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the anterolateral direction.')
conduct_stage(anterolateral_SEBT_nonop, 'non-operative',
              anterolateral_CofMs_nonop, 'anterolateral')
print("Moving on to the lateral direction of the test.")

# fourth stage of SEBT test (lateral) on non-operative leg
input('Ready for lateral orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the lateral direction.')
conduct_stage(lateral_SEBT_nonop, 'non-operative',
              lateral_CofMs_nonop, 'lateral')
print("Moving on to the posterolateral direction of the test.")

# fifth stage of SEBT test (posterolateral) on non-operative leg
input('Ready for posterolateral orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the posterolateral direction.')
conduct_stage(posterolateral_SEBT_nonop, 'non-operative',
              posterolateral_CofMs_nonop, 'posterolateral')
print("Moving on to the posterior direction of the test.")

# sixth stage of SEBT test (posterior) on non-operative leg
input('Ready for posterior orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the posterior direction.')
conduct_stage(posterior_SEBT_nonop, 'non-operative',
              posterior_CofMs_nonop, 'posterior')
print("Moving on to the posteromedial direction of the test.")

# seventh stage of SEBT test (posteriomedial) on non-operative leg
input('Ready for posteromedial orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the posterior direction.')
conduct_stage(posteromedial_SEBT_nonop, 'non-operative',
              posteromedial_CofMs_nonop, 'posteromedial')
print("Moving on to the medial direction of the test.")

# eighth stage of SEBT test (medial) on non-operative leg
input('Ready for medial orientation SEBT test on the non-operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the medial direction.')
conduct_stage(medial_SEBT_nonop, 'non-operative', medial_CofMs_nonop, 'medial')
print("SEBT testing for the non-operative leg finished. Please place the apparatus on the operative leg in order to conduct the test again.")

# first stage of SEBT test (anterior) on operative leg
input('Ready for anterior orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the anterior direction.')
conduct_stage(anterior_SEBT_op, 'operative',
              anterior_CofMs_op, 'anterior')
print("Moving on to the anteromedial direction of the test.")


# first stage of SEBT test (anteromedial) on operative leg
input('Ready for anteromedial orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the anteromedial direction.')
conduct_stage(anteromedial_SEBT_op, 'operative',
              anteromedial_CofMs_op, 'anteromedial')
print("Moving on to the anterolateral direction of the test.")


# third stage of SEBT test (anterolateral) on operative leg
input('Ready for anterolateral orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the anterolateral direction.')
conduct_stage(anterolateral_SEBT_op, 'operative',
              anterolateral_CofMs_op, 'anterolateral')
print("Moving on to the lateral direction of the test.")

# fourth stage of SEBT test (lateral) on operative leg
input('Ready for lateral orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the lateral direction.')
conduct_stage(lateral_SEBT_op, 'operative',
              lateral_CofMs_op, 'lateral')
print("Moving on to the posterolateral direction of the test.")

# fifth stage of SEBT test (posterolateral) on operative leg
input('Ready for posterolateral orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the posterolateral direction.')
conduct_stage(posterolateral_SEBT_op, 'operative',
              posterolateral_CofMs_op, 'posterolateral')
print("Moving on to the posterior direction of the test.")

# sixth stage of SEBT test (posterior) on operative leg
input('Ready for posterior orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the posterior direction.')
conduct_stage(posterior_SEBT_op, 'operative',
              posterior_CofMs_op, 'posterior')
print("Moving on to the posteromedial direction of the test.")

# seventh stage of SEBT test (posteriomedial) on operative leg
input('Ready for posteromedial orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the posterior direction.')
conduct_stage(posteromedial_SEBT_op, 'operative',
              posteromedial_CofMs_op, 'posteromedial')
print("Moving on to the medial direction of the test.")

# eighth stage of SEBT test (medial) on operative leg
input('Ready for medial orientation SEBT test on the operative leg? Press Enter to Continue.')
print('Press spacebar key upon completion of the medial direction.')
conduct_stage(medial_SEBT_op, 'operative', medial_CofMs_op, 'medial')
print("SEBT testing for the operative leg finished. Finished testing, please remove apparatus.")


# debugging purposes
SEBT_data = {
    'Anterior': [anterior_SEBT_op, anterior_SEBT_nonop],
    'Anterolateral': [anterolateral_SEBT_op, anterolateral_SEBT_nonop],
    'Anteromedial': [anteromedial_SEBT_op, anteromedial_SEBT_nonop],
    'Lateral': [lateral_SEBT_op, lateral_SEBT_nonop],
    'Medial': [medial_SEBT_op, medial_SEBT_nonop],
    'Posterolateral': [posterolateral_SEBT_op, posterolateral_SEBT_nonop],
    'Posteromedial': [posterolateral_SEBT_op, posterolateral_SEBT_nonop],
    'Posterior': [posterolateral_SEBT_op, posterolateral_SEBT_nonop]
}

CofM_data = {
    'Anterior': [anterior_CofMs_op, anterior_CofMs_nonop],
    'Anterolateral': [anterolateral_CofMs_op, anterolateral_CofMs_nonop],
    'Anteromedial': [anteromedial_CofMs_op, anteromedial_CofMs_nonop],
    'Lateral': [lateral_CofMs_op, lateral_CofMs_nonop],
    'Medial': [medial_CofMs_op, medial_CofMs_nonop],
    'Posterolateral': [posterolateral_CofMs_op, posterolateral_CofMs_nonop],
    'Posteromedial': [posteromedial_CofMs_op, posteromedial_CofMs_nonop],
    'Posterior': [posterior_CofMs_op, posterior_CofMs_nonop]
}


for item in SEBT_data:
    plot_SEBT_graph(SEBT_data[item][0], SEBT_data[item][1], item)
print("graphs saved to folder")

# debugging, remove later
print(SEBT_data)

# debugging, remove later
print(CofM_data)

# saving CofM images to folder
for item in CofM_data:
    plot_CofM_deviations(CofM_data[item][0], CofM_data[item][1], item)


# getting filenames to send as attachments
anglefiles = ['sebt/' + f for f in listdir('sebt') if isfile(join('sebt', f))]
CofMfiles = ['CofM_images/' +
             f for f in listdir('CofM_images') if isfile(join('CofM_images', f))]

file_names = anglefiles + CofMfiles

send_emails([clinician_email], file_names, SEBT_data, CofM_data)
