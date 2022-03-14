from email.mime import message
from re import M
import paho.mqtt.client as mqtt
from random import randrange, uniform
from datetime import datetime
import time
import sys

# Initiera variabler för tid
timestamp = datetime.now().strftime("%H-%M")
time2 = timestamp

# Systemargument att skicka in som topic och payload genom kommandoraden
topic = sys.argv[1]
operation = sys.argv[2]
payload = sys.argv[3]

# Öppna fil för loggning
extension = ".txt"
filename = "C:/TestWizard/Scripts/Log/testlogg__"+time2+extension
print("Path to logfile: "+filename)
time.sleep(1)
file = open(filename, "a")

# Funktion för att hålla värdet av senaste meddelande på topic

def on_message(client, userdata, message):
    global message_received
    global topic_received
    time.sleep(1)
    message_received = str(message.payload.decode("utf-8"))
    topic_received = str(message.topic)

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

#Prenumerera på angiven topic
client.subscribe("zigbee2mqtt/{}".format(topic))
file.writelines("\n")
file.writelines("Subscribed topic:" + topic + "\n" + "\n")
print("Subscribed to topic: " + topic)


# Skriv till topic med angiven operation och payload
client.publish('zigbee2mqtt/{}/set/{}'.format(topic,operation),payload)
message_sent = 'zigbee2mqtt/{}/set/{}'.format(topic,operation),payload
print("Payload sent with MQTT: " + str(message_sent))

# Skriv ut tid och datum samt vad som skickats ut på topic och tagits emot på topic
file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
file.writelines("Skickad payload: " + repr(message_sent)+"\n")

time.sleep(3)

file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
file.writelines("Mottagen status MQTT: " + topic_received + " " + message_received + " " +  "\n" + "\n")

# Plocka bort "{}" i angiven payload och sätt värde i ny variabel för jämförelse genom en for-loop

payload_chars_to_remove = "{ }"
new_payload = payload

for character in payload_chars_to_remove:
  new_payload = new_payload.replace(character, "")

# Jämföra om given payload förekommer i statusen från MQTT
if new_payload in repr(message_received):
    file.writelines("PASS - Given payload found in status-response from MQTT \n" + "\n")
else:
    file.writelines("FAIL - Given payload not found in status-response from MQTT\n" + "\n") 

# Skriv ut MQTT-information i terminalen
print("Status recieved MQTT: " + topic_received + " " + message_received)
print("End")
time.sleep(1)

# Skriv ut tid och datum samt vad som skickats ut på topic och tagits emot på topic
file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
file.writelines("Skickad payload: " + repr(message_sent) + "\n")

time.sleep(3)

file.writelines(time.strftime("%Y-%m-%d %H:%M:%S" + " "))
file.writelines("Mottagen status MQTT: " + repr(message_received) + "\n" + "\n")


# Skriv ut MQTT-information i terminalen
print(message_received)

# Avsluta loop
client.loop_stop()
