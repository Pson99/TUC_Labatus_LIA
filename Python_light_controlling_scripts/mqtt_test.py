from re import M
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time



# Ange broker
mqttBroker = "mqtt.localhost"

# Definera en klient
client = mqtt.Client("Windows")

# Anslut till broker
client.connect(mqttBroker)

# Starta loop
client.loop_start()



#Prenumerera på topic
print("Hej")
client.subscribe('zigbee2mqtt/IKEA lampa 65545')
client.publish('zigbee2mqtt/IKEA lampa 65545/set', '{ "brightness": "50" }')

client.loop_stop()