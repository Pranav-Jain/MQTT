import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	print "Connected with result code"+str(rc)
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
	client.subscribe("image")
	client.subscribe("Message")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	if msg.topic=='image':
		f = open('/Users/pranavjain/Desktop/output', 'w')
   		f.write(msg.payload)
   		print msg.payload
   		f.close()
   	else:
   		print "\nTopic: " +  msg.topic+'\nMessage: '+str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 3333, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()