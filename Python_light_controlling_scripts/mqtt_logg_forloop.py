from email.mime import message
from re import M
import paho.mqtt.client as mqtt
from random import randrange, uniform
from datetime import datetime
import time


# Öppna fil för loggning
file = open("logg.txt", "a")

# Funktion för att hålla värdet av senaste meddelande på topic

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
file.writelines("\n")
file.writelines("Prenumererar på topic: zigbee2mqtt/Ikea lampa 65545 \n" + "\n")

for x in range(5):

    # Skriv till topic med olika payload
    client.publish('zigbee2mqtt/Ikea lampa 65545/set','{ "state": "ON" }')
    message_sent = 'zigbee2mqtt/Ikea lampa 65545/set','{ "state": "ON" }'

    # Skriv ut tid och datum samt vad som skickats ut på topic och tagits emot på topic
    file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
    file.writelines("Skickad payload: " + repr(message_sent)+"\n")

    time.sleep(3)

    file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
    file.writelines("Mottagen status MQTT: " + message_received + " " +  "\n" + "\n")

    # Jämföra om given payload förekommer i statusen från MQTT
    if '"state":"ON"' in repr(message_received):
        file.writelines("PASS - Given payload förekommer i status-svar från MQTT \n" + "\n")
    else:
        file.writelines("FAIL - Given payload förekommer inte i status-svar från MQTT\n" + "\n") 

    # Skriv ut MQTT-information i terminalen
    print(message_received)

    # Paus i 3 sekunder och stäng sedan av lampan
    time.sleep(3)

    client.publish('zigbee2mqtt/Ikea lampa 65545/set','{ "state": "OFF" }')
    message_sent = 'zigbee2mqtt/Ikea lampa 65545/set','{ "state": "OFF" }'

    # Skriv ut tid och datum samt vad som skickats ut på topic och tagits emot på topic
    file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
    file.writelines("Skickad payload: " + repr(message_sent) + "\n")

    time.sleep(3)

    file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
    file.writelines("Mottagen status MQTT: " + repr(message_received) + "\n" + "\n")

    # Jämföra om given payload förekommer i statusen från MQTT
    if '"state":"OFF"' in repr(message_received):
        file.writelines("PASS - Given payload förekommer i status-svar från MQTT \n" + "\n")
    else:
        file.writelines("FAIL - Given payload förekommer inte i status-svar från MQTT\n" + "\n") 

    # Skriv ut MQTT-information i terminalen
    print(message_received)

# Avsluta loop
client.loop_stop()
