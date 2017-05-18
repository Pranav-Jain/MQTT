import paho.mqtt.client as mqtt

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
	f=open(file, "rb")
	fileContent = f.read()
	byteArr = bytearray(fileContent)
	mqttc.publish("image",byteArr)
else:
	print "Wrong Choice"
mqttc.loop(2)

