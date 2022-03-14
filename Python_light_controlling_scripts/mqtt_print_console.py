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
client.subscribe("zigbee2mqtt/Ikea lampa 65545")


# Skriv till topic med olika payload
client.publish('zigbee2mqtt/Ikea lampa 65545/set','{ "state": "ON" }')
payload = 'zigbee2mqtt/Ikea lampa 65545/set','{ "state": "ON" }'
time.sleep(5)
print(message_received)
print(payload)

# Paus i 5 sekunder och stäng sedan av lampan
time.sleep(5)
client.publish('zigbee2mqtt/Ikea lampa 65545/set','{ "state": "OFF" }')
time.sleep(5)
print(message_received)

# Avsluta loop
client.loop_stop()
