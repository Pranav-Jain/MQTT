import paho.mqtt.client as mqtt
import json

client_id = "Pranav"
server = "localhost"
port = 3333

mqttc = mqtt.Client("P_"+client_id)
mqttc.connect(server, port)
print "1. File"
print "2. Message"
option = raw_input("\nEnter Choice: ")
if option=='2':
	message = raw_input("\nEnter the message: ")
	mqttc.publish("Message", client_id+"@"+message)
elif option=='1':
	file = raw_input("Enter file path: ")
	f=open(file, "r")
	fileContent = f.read()
	#encoded = base64.encodestring(fileContent)

	#byteArr = bytearray(fileContent)
	mqttc.publish("image",json.JSONEncoder().encode(fileContent),0)
else:
	print "Wrong Choice"
mqttc.loop(2)
