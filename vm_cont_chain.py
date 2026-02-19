# vm_cont_chain

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):

    print("Connected to server (i.e., broker) with result code "+str(rc))
    #replace user with your USC username in all subscriptions
    client.subscribe("selenazh/ping")
        
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("selenazh/ping", on_message_from_ping)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback.
def on_message_from_ping(client, userdata, message):
   num = int(message.payload.decode("utf-8", errors="replace").strip())
   print("Custom callback  - Ping: "+message.payload.decode())
   client.publish("selenazh/pong", f"{num+1}")
   print("Publishing pong")


if __name__ == '__main__':
    
    ip_address = 0 #'192.168.0.176'
    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    #client.connect(host=ip_address, port=1883, keepalive=60)
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_forever()




