import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("localhost", 3333)
mqttc.publish("hello/world", "hello vbkj")
mqttc.loop(2)

