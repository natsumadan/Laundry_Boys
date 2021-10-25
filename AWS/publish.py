# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
import threading

import re
import paho.mqtt.client as mqtt2


#### RECEIVE DATA FROM EC2
def on_connect(client, userdata, flags, rc): # func for making connection
        print("Connected to MQTT")
        print("Connection returned result: " + str(rc))
        client.subscribe("group6Data")
def on_message(client, userdata, msg): # Func for Sending msg
        print(msg.topic+" "+str(msg.payload))
        lightArr = re.findall("\d+",str(msg.payload))
        light = lightArr[4]
        num = re.findall("\d+\.\d+",str(msg.payload))
        humidity = num[0]
        temp = num[1]
        wind = num[2]
        print('Only numbers are:')
        print(num)
        print(humidity)
        print(temp)
        print(light)
        print(wind)
        
        t.sleep(0.5)
        #######

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
        ENDPOINT = "a1jepn4zys8yy5-ats.iot.us-east-1.amazonaws.com"
        CLIENT_ID = "RaspberyPi_One"
        PATH_TO_CERT = "certificates/Advanced.cert.pem"
        PATH_TO_KEY = "certificates/Advanced.private.key"
        PATH_TO_ROOT = "certificates/root.pem"




        #TOPICS:
        TOPIC_WIND = "laundry/wind"
        
        MESSAGE_WIND = wind 

        TOPIC_HUMIDITY = "laundry/humidity"
       
        MESSAGE_HUMIDITY = humidity 

        TOPIC_TEMP = "laundry/temperature"

        MESSAGE_TEMP = temp

        TOPIC_PHOTO = "laundry/photoresistor"
      
        MESSAGE_PHOTO = light




        # Spin up resources
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        mqtt_connection = mqtt_connection_builder.mtls_from_path(
                    endpoint=ENDPOINT,
                    cert_filepath=PATH_TO_CERT,
                    pri_key_filepath=PATH_TO_KEY,
                    client_bootstrap=client_bootstrap,
                    ca_filepath=PATH_TO_ROOT,
                    client_id=CLIENT_ID,
                    clean_session=False,
                    keep_alive_secs=6
                    )
        print("Connecting to {} with client ID '{}'...".format(
                ENDPOINT, CLIENT_ID))
        # Make the connect() call
        connect_future = mqtt_connection.connect()
        # Future.result() waits until a result is available
        connect_future.result()
        print("Connected!")
        # Publish message to server desired number of times.
        print('Begin Publish')

        
        i = 0
        t.sleep(2)
       
        def wind_sensor(TOPIC_WIND, MESSAGE_WIND):
            data_wind = "{}".format(MESSAGE_WIND)
            message_wind = {"Wind" : float(data_wind)}
            mqtt_connection.publish(topic=TOPIC_WIND, payload=json.dumps(message_wind), qos=mqtt.QoS.AT_LEAST_ONCE)
            print('Publish wind sensor data')
            print(MESSAGE_WIND)
            t.sleep(1)
        def hum_sensor(TOPIC_HUMIDITY, MESSAGE_HUMIDITY):
            data_hum = "{}".format(MESSAGE_HUMIDITY)
            message_hum = {"Humidity" : float(data_hum)}
            mqtt_connection.publish(topic=TOPIC_HUMIDITY, payload=json.dumps(message_hum), qos=mqtt.QoS.AT_LEAST_ONCE)
            print('Publish humidity sensor data')
            print(MESSAGE_HUMIDITY)
            t.sleep(1)
        def temp_sensor(TOPIC_TEMP, MESSAGE_TEMP):
            data_temp = "{}".format(MESSAGE_TEMP)
            message_temp = {"Temperature" : float(data_temp)}
            mqtt_connection.publish(topic=TOPIC_TEMP, payload=json.dumps(message_temp), qos=mqtt.QoS.AT_LEAST_ONCE)
            print('Publish temperature sensor data')
            print(MESSAGE_TEMP)
            t.sleep(1)
        def photo_sensor(TOPIC_PHOTO, MESSAGE_PHOTO):
            data_photo = "{}".format(MESSAGE_PHOTO)
            message_photo = {"Photoresistor" : int(data_photo)}
            mqtt_connection.publish(topic=TOPIC_PHOTO, payload=json.dumps(message_photo), qos=mqtt.QoS.AT_LEAST_ONCE)
            print('Publish photoresistor sensor data')
            print(MESSAGE_PHOTO)
            t.sleep(1)

            #Threading
        t_wind = threading.Thread(target=wind_sensor, args=(TOPIC_WIND, MESSAGE_WIND))
        t_hum = threading.Thread(target=hum_sensor, args=(TOPIC_HUMIDITY, MESSAGE_HUMIDITY)) 
        t_temp = threading.Thread(target=temp_sensor, args=(TOPIC_TEMP, MESSAGE_TEMP)) 
        t_photo = threading.Thread(target=photo_sensor, args=(TOPIC_PHOTO, MESSAGE_PHOTO))


        t_wind.start()
        t_temp.start()
        t_hum.start()
        t_photo.start()

        t_wind.join()
        t_temp.join()
        t_hum.join()
        t_photo.join()

        t.sleep(0.5)
    

            
        i += 1
        print('Total number of publishings is {}'.format(i))
        t.sleep(0.5)

                #######
        
                
        
client = mqtt2.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("3.25.68.204", 1883, 60)
client.loop_forever()





    

###### WE CAN USE THE FOLLOWING FUCNTION TO STOP PYTHON WITH A COMMAND WITHOUT CMD+C  begin
# print('Publish End')
# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()
###### WE CAN USE THE FOLLOWING FUCNTION TO STOP PYTHON WITH A COMMAND WITHOUT CMD+C  end