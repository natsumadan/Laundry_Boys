import serial
import time, sys
import string 
import paho.mqtt.publish as publish
from sense_hat import SenseHat


#read and write data from and to arduino serially 
# input the correct rf channel into the parameter, rfcomm0 is normally the defult for the first connection 
# input the IP address of the aws broker 

ser = serial.Serial("/dev/rfcomm4", 9600)

#using sense hat led as indicator
sense = SenseHat()
#setting colors
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)


while True:
	if ser.in_waiting > 0:
		rawserial = ser.readline()
		rawstring = rawserial.decode('utf8').strip('\r\n')

		# Split the whole string in to a list and take out the information needed 

		x = rawstring.strip().split()

		# input the index of each information 

		wind = x[14] #Insert wind speed index here 

		humid = x[1].split("%")
		temp = x[3].split("C")
		light = x[12]
		print(" ")

		#----------------------Final form of the required data ---------------------------

		th = ("Humidity: " + str(humid[0]) + " Temperature: " + str(temp[0]))
		li = (" Light intensity: " + light)
		wi = (" Wind Level: " + wind)
		print(th + li+ wi)


		
		#----------------------Set Threshold Control---------------------------------------
		#Set threshold control 
		H = float(humid[0])
		T = float(temp[0])
		L = float(light)
		W = float(wind)
        
		if (H < 70 and T > 20 and L > 140 and W>3 and W <35):
			nmsg = "Level1! The weather right now is suitable for drying laundry!!!"
			#sense.show_message("Y", text_colour = green)
			sense.show_letter("Y", green)
		elif (H < 70 and T > 30 and L > 550 and W > 20 and W < 35):
			nmsg = "Level2! Go do your laundry now!!! The weather is great!!!"
			#sense.show_message("G", text_colour = yellow)
			sense.show_letter("G", yellow)
		else:
			nmsg = "Level0! Ops, the weather is not too good right now, you might want to do laundry at another time."
			#sense.show_message("N", text_colour = red)
			sense.show_letter("N", red)

		print(nmsg)
		

		#----------------------Publish the Information-------------------------------------
		publish.single("group6Data", th+li+wi, hostname="3.25.68.204")
		print("Done")
		publish.single("group6Notification", nmsg, hostname="3.25.68.204")
		print("Done")
		
		#---------------------Sleep 1 seconds and clean the sense hat ---------------------
		#---------------------KeyboardInterrupt to quit the program -----------------------
		try :
			pass

		except KeyboardInterrupt:
			sense.clear()
			sys.exit()



