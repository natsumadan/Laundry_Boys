import serial
import time
import sys
import json
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
from threading import Thread
from abc import ABCMeta, abstractmethod


class ITopic:
    def getTopic(self):
        return self.mName

    @abstractmethod
    def proc(self, msg):
        pass


class NotificationTopic(ITopic):
    def __init__(self):
        self.mName = 'group6Notification'

    def proc(self, msg):
        print(self.mName, ' : ', msg.payload.decode("utf-8"))
        # to process message for the topic of Notification
        # this topic will contain laundry indication and weather summary for user.


class DataTopic(ITopic):
    def __init__(self):
        self.mName = 'group6Data'

    def proc(self, msg):
        print(self.mName, ' : ', msg.payload.decode("utf-8"))
        # to process message for topic of Notification
        # this topic will contain data of humidity, temperature, light intensity and wind level


class MQTTClient:
    def __init__(self, addr, topic):
        self.mClient = mqtt.Client(userdata=self)
        self.mClient.on_connect = self.on_connect
        self.mClient.on_message = self.on_message
        self.mClient.connect(addr, 1883, 60)
        self.mTopic = topic
        time.sleep(1)

    @staticmethod
    def on_connect(client, userdata, flag, rc):
        print("Connected to MQTT")
        print("Connection returned result: " + str(rc))

        userdata.mClient.subscribe(userdata.mTopic.mName)

    @staticmethod
    def on_message(client, userdata, msg):

        userdata.mTopic.proc(msg)
        x = msg.payload.decode("utf-8").strip().split()

        # connect to bluetooth chip that control 3 Leds
        ser = serial.Serial("/dev/rfcomm3", 9600)
        ser.write(str.encode('Start\r\n'))

        # control command for Leds
        if(x[0] == "Level0!"):
            ser.write(b"RedLed_ON\n")
            ser.write(b"GreenLed_OFF\n")
            ser.write(b"YellowLed_OFF\n")
        elif(x[0] == "Level1!"):
            ser.write(b"RedLed_OFF\n")
            ser.write(b"GreenLed_ON\n")
            ser.write(b"YellowLed_OFF\n")
        elif(x[0] == "Level2!"):
            ser.write(b"RedLed_OFF\n")
            ser.write(b"GreenLed_OFF\n")
            ser.write(b"YellowLed_ON\n")
        else:
            ser.write(b"RedLed_OFF\n")
            ser.write(b"GreenLed_OFF\n")
            ser.write(b"YellowLed_OFF\n")

    def start(self):
        self.mClient.loop_start()

    def stop(self):
        self.mClient.loop_stop(True)


def main():
    client1 = MQTTClient("3.25.68.204", NotificationTopic())
    client1.start()

    client2 = MQTTClient("3.25.68.204", DataTopic())
    client2.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client1.stop()
        client2.stop()
        pass


if __name__ == "__main__":
    main()
