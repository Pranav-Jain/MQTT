import paho.mqtt.client as mqtt
import json

client_id = "Pranav"

def on_connect(client, userdata, rc):
	print "Connected with result code"+str(rc)

	client.subscribe("image")
	client.subscribe("Message")

def on_message(client, userdata, msg):
	if msg.topic=='image':
		#print decoded
		f = open('/Users/pranavjain/Desktop/output', 'w')
   		f.write(json.loads(msg.payload))
   		f.close()
   		print "File Sent"
   	else:
   		f = msg.payload.find("@")
   		print "\nTopic: " +  msg.topic+ '\nFrom: '+ str(msg.payload[:f]) + '\nMessage: '+str(msg.payload[f+1:])

client = mqtt.Client("S_" + client_id)
client.connect("localhost", 3333, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()