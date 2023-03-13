#Author: Group 23 (Miguel, Akanksha, Dorian)
#Date: March 12th 2023
#Purpose: To interface the data acquisition with the esp32 DAQ

import bluetooth as bt

class bluetoothTelephone:
    def __init__(self):
    
        self.targetName = "ESP32Group23"
        self.targetAddress = None
        self.successfullConnect = False

        #Upon initialization find the esp32 and if not found throw error
        nearby_devices = bt.discover_devices()

        for btaddr in nearby_devices:
            if self.targetName == bt.lookup_name(btaddr):
                self.targetAddress = btaddr
                break
        
        #Connect to the esp32 if found
        port = 1
        self.sock = bt.BluetoothSocket(bt.RFCOMM)
        self.sock.settimeout(30) #Sets the timeout to 30 seconds because the connection should not take any longer to establish
        try:
            self.sock.connect((btaddr, port))
        except OSError:
            print("Was unable to connect to target address:", self.targetAddress)
            print("If the target address is 'none', this means that your target device was not found :(")    
        else:
            print("Connection successfully established")
            #Raise flag
            self.successfullConnect = True

        #Returns if the connection was sucessfully established

    def getData(self):
        #Receive data from sensors attached to the esp32
        #Data reception is implemented using a call and response model - if you write to the esp32 the esp32 will respond with the sensor data

        self.sock.send("1")
        loadcell1 = int.from_bytes(self.sock.recv(1))
        loadcell2 = int.from_bytes(self.sock.recv(1))
        loadcell3 = int.from_bytes(self.sock.recv(1))
        loadcell4 = int.from_bytes(self.sock.recv(1))
        kneeAngle = int.from_bytes(self.sock.recv(1))
        EMGVal = int.from_bytes(self.sock.recv(1))

        return [loadcell1,loadcell2,loadcell3,loadcell4] , kneeAngle, EMGVal
        
