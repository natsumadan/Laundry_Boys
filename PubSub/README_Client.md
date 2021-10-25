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