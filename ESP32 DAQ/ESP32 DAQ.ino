#include "HX711.h"
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include "BluetoothSerial.h"

// HX711 circuit wiring and loadcell variables
const int LOADCELL1_DOUT_PIN = 13;
const int LOADCELL1_SCK_PIN = 12;

const int LOADCELL2_DOUT_PIN = 25;
const int LOADCELL2_SCK_PIN = 26;

const int LOADCELL3_DOUT_PIN = 27;
const int LOADCELL3_SCK_PIN = 14;

const int LOADCELL4_DOUT_PIN = 4;
const int LOADCELL4_SCK_PIN = 0;

const long LOADCELL_DIVIDER = 5000;//5895655;

//Names of the individual loadcells
HX711 loadcell1;
HX711 loadcell2;
HX711 loadcell3;
HX711 loadcell4;

//Reading values will be stored in these variables
int loadcellVal1 = 0;
int loadcellVal2 = 0;
int loadcellVal3 = 0;
int loadcellVal4 = 0;

//Aggregate total before averaging
float loadcellTotal1;
float loadcellTotal2;
float loadcellTotal3;
float loadcellTotal4;

//Average readings across x number of samples
float loadcellAvg1;
float loadcellAvg2;
float loadcellAvg3;
float loadcellAvg4;

int loadcellSamples = 10; //Number of samples used to get average
int loadcellSampleDelay = 5; //10 ms

//------------------------------------------------------------------------------------------//

//BNO circuit wiring and variables
int BNO055_SAMPLERATE_DELAY_MS = 5;
int bnoSamples = 10; //Number of samples used to get average

//I2C communication
Adafruit_BNO055 bnoProx = Adafruit_BNO055(-1, 0x28, &Wire);
Adafruit_BNO055 bnoDist = Adafruit_BNO055(-1, 0x28, &Wire1);

//Initialize variables for x angles for both the proximal and the distal sensor
float Xprox = 0;
float Xdist = 0;

//Initialize summation variables for calculating the average angle
float totalProx = 0;
float totalDist = 0;

//Initialize the vector variables to hold the x y and z angles
imu::Vector<3> eulerProx;
imu::Vector<3> eulerDist;

//Initialize the averaged X angles
float XproxAvg = 0;
float XdistAvg = 0;

//Initialize the difference in angle between the two sensors
float kneeExtensionAngle = 0;

#define SDA_2 33
#define SCL_2 32

//------------------------------------------------------------------------------------------//

//EMG circuit wiring and variables
int EMGPin = 34;
float EMGReading;
float EMGTotal;
float EMGAvg;
int EMGSampleDelay = 5;
int EMGSamples = 10;

//------------------------------------------------------------------------------------------//

//Bluetooth initializations
BluetoothSerial SerialBT;

void setup() {
  // Setup for the loadcells
  Serial.begin(115200);
  
  loadcell1.begin(LOADCELL1_DOUT_PIN, LOADCELL1_SCK_PIN);
  loadcell1.set_scale(LOADCELL_DIVIDER);

  loadcell2.begin(LOADCELL2_DOUT_PIN, LOADCELL2_SCK_PIN);
  loadcell2.set_scale(LOADCELL_DIVIDER);

  loadcell3.begin(LOADCELL3_DOUT_PIN, LOADCELL3_SCK_PIN);
  loadcell3.set_scale(LOADCELL_DIVIDER);

  loadcell4.begin(LOADCELL4_DOUT_PIN, LOADCELL4_SCK_PIN);
  loadcell4.set_scale(LOADCELL_DIVIDER);

  loadcell1.tare();
  loadcell2.tare();
  loadcell3.tare();
  loadcell4.tare();

  //Setup for BNOs
  Wire.begin();
  Wire1.begin(SDA_2, SCL_2, 100000);
  
  bnoProx.begin();
  bnoDist.begin();

  bnoProx.setExtCrystalUse(true);
  bnoDist.setExtCrystalUse(true);

  //Setup for EMG

  //Setup for bluetooth communication
  SerialBT.begin("ESP32Group23"); //Bluetooth device name
}

void loop() {

  //Loadcell DAQ
  loadcellTotal1 = 0;
  loadcellTotal2 = 0;
  loadcellTotal3 = 0;
  loadcellTotal4 = 0;

  for(int i=0; i<loadcellSamples; i++)
  {
    //Take the average of a number of values

    //Check if the ADC is ready
    if(loadcell1.wait_ready_timeout(10)){
      loadcellVal1 = loadcell1.get_units(1);
      //If not ready, loadCellVal value stays the same
    }
    if(loadcell2.wait_ready_timeout(10)){
      loadcellVal2 = loadcell2.get_units(1);
    }
    if(loadcell3.wait_ready_timeout(10)){
      loadcellVal3 = loadcell3.get_units(1);
    }
    if(loadcell4.wait_ready_timeout(10)){
      loadcellVal4 = loadcell4.get_units(1);
    }

    loadcellTotal1 += loadcellVal1;
    loadcellTotal2 += loadcellVal2;
    loadcellTotal3 += loadcellVal3;
    loadcellTotal4 += loadcellVal4;

    delay(loadcellSampleDelay);
  }
  
  //Find the average values of the samples taken
  loadcellAvg1 = loadcellTotal1/loadcellSamples;
  loadcellAvg2 = loadcellTotal2/loadcellSamples;
  loadcellAvg3 = loadcellTotal3/loadcellSamples;
  loadcellAvg4 = loadcellTotal4/loadcellSamples;

  //Serial.print("Loadcell weight: ");
  //Serial.println(loadcellAvg1);

  //BNO055 DAQ
  totalProx = 0;
  totalDist = 0; 
  
  // Take the average of the last # of samples
  for (int i = 0; i<bnoSamples; i++)
  {
    //Get the Euler vectors from both sensors
    eulerProx = bnoProx.getVector(Adafruit_BNO055::VECTOR_EULER);
    eulerDist = bnoDist.getVector(Adafruit_BNO055::VECTOR_EULER);

    //Obtain the current X angle
    Xprox = eulerProx.x();
    Xdist = eulerDist.x();

    //Add current angle to total
    totalProx += Xprox;
    totalDist += Xdist;
    delay(BNO055_SAMPLERATE_DELAY_MS);
  }

  XproxAvg = totalProx/bnoSamples;
  XdistAvg = totalDist/bnoSamples;

  //Find the difference in the angle between the two BNO055 sensors
  kneeExtensionAngle = abs(XproxAvg - XdistAvg);

  //If one of the sensors is reding an angle of ~360 (this happens as the sensor rotates in the negative direction after attaining 0 degrees)
  if (kneeExtensionAngle > 180)
  {
    kneeExtensionAngle = abs(kneeExtensionAngle - 360);
  }

  //Serial.print("Knee extension angle: ");
  //Serial.println(180 - kneeExtensionAngle);
  //Serial.println("°");

  //Serial.print("BNO 1: ");
  //Serial.println(XproxAvg);
  //Serial.print("BNO 2: ");
  //Serial.println(XdistAvg);

  //EMG DAQ
  EMGTotal = 0;
  
  // Take the average of the last # of samples
  for (int i = 0; i<EMGSamples; i++)
  {
    //reading the EMG analog pin
    EMGReading = analogRead(EMGPin);    
    EMGTotal += EMGReading;
    delay(EMGSampleDelay);
  }

  EMGAvg = EMGTotal/EMGSamples;

  //Serial.print("EMG Value: ");
  //Serial.println(EMGAvg);

  //Transmit over bluetooth
  if (SerialBT.available())
  {
    //Implements a call and response model - if the esp32 is written to it will respond with the acquired sensor data
    SerialBT.write((int)loadcellAvg1); //Cast as integer to comply with the limitations of the write function
    SerialBT.write((int)loadcellAvg2);
    SerialBT.write((int)loadcellAvg3);
    SerialBT.write((int)loadcellAvg4);
    SerialBT.write((int)kneeExtensionAngle);
    SerialBT.write((int)EMGAvg);

    //Following lines of code were used for testing purposes
    //Serial.println(SerialBT.read());
    //Serial.print("Loadcell: ");
    //Serial.println((int)loadcellAvg1);
    //Serial.print("BNO angle: ");
    //Serial.println((int)kneeExtensionAngle);
  }
  
}
