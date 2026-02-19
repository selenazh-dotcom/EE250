# vm_start_chain
# can't connect to the RPI for some reason, using public broker

import paho.mqtt.client as mqtt
import time
import socket

STARTNUM = 0

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("selenazh/pong")
    client.message_callback_add("selenazh/pong", on_message_from_pong)
    
    client.publish("selenazh/ping", f"{STARTNUM}")
    print("Sending first ping")
    
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))
    
# receiving from vm_cont_chain
def on_message_from_pong(client, userdata, message):
   num = int(message.payload.decode("utf-8", errors="replace").strip())
   print("Custom callback  - Pong: "+message.payload.decode())
   client.publish("selenazh/ping", f"{num+1}")
   print("Publishing ping")
   

if __name__ == '__main__':
    #get IP address
    ip_address= 0 #'192.168.0.176' 
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_message = on_message
    client.on_connect = on_connect

    #client.connect(host=ip_address, port=1883, keepalive=60)
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_forever()     





