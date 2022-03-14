from re import M
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time


# Funktion för att skriva ut meddelanden på topic
#def on_message(client, userdata, message):
    #print("Received state:" +str(message.payload.decode("utf-8")))

def on_message(client, userdata, message):
    global message_received
    time.sleep(1)
    message_received = str(message.payload.decode("utf-8"))

# Ange broker
mqttBroker = "mqtt.localhost"

# Definera en klient
client = mqtt.Client("Linux-dator")

# Anslut till broker
client.connect(mqttBroker)

# Starta loop
client.loop_start()

# Skriv ut ev. meddelanden på topic
client.on_message = on_message

#Prenumerera på topic
print("Hej")
client.subscribe('zigbee2mqtt/Aqara temperature sensor')

time.sleep(5)

for x in range(10):
    x = message_received
    time.sleep(2)
    print(x)

time.sleep(10)
client.loop_stop()