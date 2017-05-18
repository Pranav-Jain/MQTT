import paho.mqtt.client as mqtt

mqttc = mqtt.Client("Pranav")
mqttc.connect("localhost", 3333)
print "1. File"
print "2. Message"
option = raw_input("\nEnter Choice: ")
if option=='2':
	message = raw_input("\nEnter the message: ")
	mqttc.publish("Message", message)              #To publish a message
elif option=='1':
	file = raw_input("Enter file path: ")
	f=open(file, "rb")
	fileContent = f.read()
	byteArr = bytearray(fileContent)
	mqttc.publish("image",byteArr,0)
else:
	print "Wrong Choice"
mqttc.loop(2)

