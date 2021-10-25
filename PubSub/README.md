==========================================================================================
Publisher Side 
Description:

This is the publisher program written in Python

The following steps explain what this program does:

- This program established Serial connection to Teensy 1 via a bluetooth module HC-05

- It will receive data from the sensors on Teensy 1 via bluetooth rfcomm channel 

- The received string is being processed and the required infomration are extracted from the rawstring. 

- Using extracted information to reconstructure a new string that contain humidity, temperature, light intensity and windspeed in a readable format. 

- Set thresholds of suitable weather for drying clothes, and use Raspberry pi SenseHat to display different messages according to the weather conditions and print out recommendation messages.

- publish the data string and recommendation message to the broker on AWS EC2 in their own topic. 


Dependencies:
python3
serial
time, sys
string
paho.mqtt
sense_hat

Executing program:
- Install python3, python3-pip, and paho-mqtt on the rapsberry pi
	* sudo apt-get install python3-pip
	* sudo pip3 install paho-mqtt

- Attach the SenseHat on the rapsberry pi, install sensehat library on the raspberry pi
	* sudo apt update
	* sudo apt install sense-hat
	* sudo reboot

- Connect to the bluetooth on raspberry pi and find out the rfcomm channel 

- Input the rfcomm channel in the code (the line of establishing bluetooth connection)

- Run this program with python3

- Exit this program by pressing ctrl+c

===========================================================================================================

Client Side Code

Description:

This is the client program written in Python

The following steps explain what this program does:

- Topic classes are defined, this program subscribes to two topics on the broker

- Client class is defined, multiple functions are created for client to make connection, topic subscription, display messages, and process the messages

- The client also establishes bluetooth connection with the second teensy, and send commands to the second teensy to control the LEDs

- This Program uses threading to run two clients that subcribe to different topics at the same time. 


Dependencies:
python3
serial 
sys
json
paho.mqtt
threading

Executing program: 

- Install python3, python3-pip, and paho-mqtt on the rapsberry pi (or your host device)
	* sudo apt-get install python3-pip
	* sudo pip3 install paho-mqtt

- Connect to the bluetooth on raspberry pi and find out the rfcomm channel 

- Input the rfcomm channel in the code (the line of establishing bluetooth connection)

- Run this program with python3

- Exit this program by pressing ctrl+c
