Tier 3 Cloud implementation of the project

The file is written and executed in Python

Here we:

1) Fetch data from sensors by subscribing to EC2 AWS virtual machine via paho mqtt client

2) Take numerical values out of the received string

3) Send them as 4 different topics by publishing to IoT Core

4) Further this data is used for email and SMS notification using SNS AWS service. It is also sent to IoT Analytics and then pipelined to Quicksight in order to visualize.
    
        Python file ->   IoT Core ->   a) SNS 
                                  ->   b) IoT analytics - > Quicksight


In order to run the code:

1) Run: "sudo pip3 install paho-mqtt" (broker that subscribes to EC2)

2) Run “sudo pip3 install awsiotsdk” (broker that published to IoW Core)

3) User has to make sure the certificates are present in the directory of the code

4) Run “python3 publish.py” in terminal 


