Description:

This is the client program written in Python

The following steps explain what this program does:

- Topic classes are defined, this program subscribes to two topics on the broker

- Client class is defined, multiple functions are created for client to make connection, topic subscription, display messages, and process the messages

- The client also establishes bluetooth connection with the second teensy, and send commands to the second teensy to control the LEDs

- This Program uses threading to run two clients that subcribe to different topics at the same time. 