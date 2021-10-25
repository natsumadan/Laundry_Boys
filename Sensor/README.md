Description:

This is the Teensy program written in C++

The following steps explain what this program does:

- This program initialize serial connection, bluetooth connection, and 3 LEDs on a Teensy board

- In the loop function, it will keep receiving data from bluetooth module and running ledControl() which control 3 LEDs on and off based on the received data from bluetooth. 


Hardware required:

- control board such as Teensy (we used in our application), or arduino uno/mega.
- breadborad 
- wires
- LEDs 
- resistors 


Executing program: 

- compile the program, load it to the teensy board 

- build a circuit with teensy, HC-05 (or your choice of bluetooth model), and 3 LEDs in different colors

- Power up the teensy 
