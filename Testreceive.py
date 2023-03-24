#Author: Group 23 (Miguel, Akanksha, Dorian)
#Date: March 12th 2023
#Purpose: Showcase how to use the DataReceive.py library


#READ THIS COMMENT OR ELSE THERE WILL BE PROBLEMS

'''Make sure to check the value of bluetoothCommObject.successfullConnect
This value will tell you if you're connected or not - please build a contingency plan
in case connection is not successfully established (whether that is try again or raise some exception

Note: you only need to check if the connection was successfully established at the start as the connection persists as long as the object is alive'''

import DataReceive #Name of the file containing the bluetooth serial object
import time

#Make the bluetooth object that will establish the connect and send back data
bluetoothCommObject = DataReceive.bluetoothTelephone()
if (bluetoothCommObject.successfullConnect == True):
    print("Connection was successfully established \n")
else:
    print("Connection was not successfully established")

while(1):

    #Call the get data function - it will return an array containing the load cell values and separately it will return the knee angle and the EMG raw signal
    loadcells, bno, emg = bluetoothCommObject.getData()

    print(loadcells)
    print(bno)
    print(emg)

    #You must repeatidly call the getData() method to get new data, it won't run in the background and automatically refresh your values
    #You ran call the getData() function at a maximum rate of 1 call every 150 ms
    
    #If you do run this code faster than 150 ms, the sock.recv() function will wait until there's new data to be received which is only put onto the socket every 150 ms so in fact we're hard limited to a max sampling rate of once every 150 ms.
    #This rate could be improved but only by altering the arduino code - talk to Dorian Knight if this is an issue
    time.sleep(0.150) #Sleep for 1 second