# Importera olika bibliotek

from re import M
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# Ange adressen till MQTT-brokern
mqttBroker = "mqtt.localhost"

# Definera en klient
client = mqtt.Client("Linux-dator")

# Anslut klienten till brokern
client.connect(mqttBroker)

######################################

# Användarens val av lampa att styra
# Beroende på input-värde så returnerar funktionen input-värde eller avslutar programmet

def lamp_choice():
    while True:
        try:
            value = input("Ange ett lampnummer (65542, 65543, 65545) att styra eller ange Q för att avsluta.\n")
            if value == "65542" or value == "65543" or value == "65545":
                return value
            elif value == "Q" or value == "q":
                quit()
        except:
            print("Du skrev in ett felaktigt värde. Försök igen")  

# Användarens val av vilken operation som ska utföras på vald lampa
# Beroende på input-värde returnerar funktionen olika värden

def user_choice():
    while True:
        try:
            value = int(input("Välj vilken operation du vill utföra. \n Välj 1 för att tända/släcka. Välj 2 för att dimra och 3 för att ändra färgtemperatur \n"))
            if value == 1:
                return value
            elif value == 2:
                return value
            elif value == 3:
                return value
        except:
            print("Du skrev in ett felaktigt värde. Försök igen.")

# Funktion för av/på i de fall användaren väljer detta som operation
# Beroende på input-värde ändrar variabeln payload värde

def lamp_switch():
    while True:
        try:
            value = int(input("Ange 1 för att tända och 0 för att släcka. \n"))
            if value == 1:
                payload = '{ "state": "ON" }'
            elif value == 0:
                payload = '{ "state": "OFF" }'
            return payload
        except:
            print("Du skrev in ett felaktigt värde. Försök igen.")   

# Funktion för ljusstyrka i de fall användaren väljer detta som operation
# Beroende på input-värde ändrar variabeln payload sitt värde för ljusstyrkan

def lamp_brightness():
    while True:
        try:
            brightness_level = int(input("Ange ett tal mellan 0-254 där 254 är full ljusstyrka. \n "))
            if brightness_level >= 0 or brightness_level <= 254:
                payload = '{ "brightness": %s }' % str(brightness_level)
                return payload
        except:
            print("Du skrev in ett felaktigt värde. Ange ett tal mellan 0-254.")

# Funktion för färgtemperatur i de fall användaren väljer detta som operation
# Beroende på input-värde ändrar variabeln payload sitt värde för färgtemperaturen

def lamp_color_temperature():
    while True:
        try:
            color_temperature_level = int(input("Ange ett tal mellan 250 - 454 där 454 motsvarar den varmaste färgtemperaturen. \n "))
            if color_temperature_level >= 250 or color_temperature_level <= 454:
                payload = '{ "color_temp": %s }' % str(color_temperature_level)
                return payload
        except:
            print("Du skrev in ett felaktigt värde. Ange ett tal mellan 250-454.")

######################################

# Programmets "main-metod". De olika funktionerna ovan körs i sekvens och anropas med hjälp av variablerna "lamp_number" samt "user_operation_choice"

while True:
    lamp_number = lamp_choice()
    user_operation_choice = user_choice()

    if user_operation_choice == 1:
        operation = lamp_switch()
    elif user_operation_choice == 2:
        operation = lamp_brightness()
    else:
        operation = lamp_color_temperature()

    # Topic styrs av användarens tidigare val av lampa
    topic = 'zigbee2mqtt/Ikea lampa {}/set'.format(lamp_number)

    # Publicera/skriv till topic med vald payload/operation
    client.publish((topic),(operation))

