import RPi.GPIO as GPIO
import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()


# Define the GPIO pins connected to the buttons
BUTTON1_PIN = 23  # Change this to the pin you've connected button 1 to
BUTTON2_PIN = 18  # Change this to the pin you've connected button 2 to

# Beeminder settings
BEEMINDER_GOAL1 = 'debt'  # Replace with your first Beeminder goal
BEEMINDER_GOAL2 = 'triathlon'  # Replace with your second Beeminder goal


def send_beeminder_datapoint(goal, value=1):
    BEEMINDER_URL = f"https://www.beeminder.com/api/v1/users/{os.environ.get('BEEMINDER_USER')}/goals/{goal}/datapoints.json"
    data = {
        'value': value,
        'auth_token': os.environ.get('BEEMINDER_AUTH_TOKEN')
    }
    response = requests.post(BEEMINDER_URL, data=data)
    if response.status_code == 200:
        print(f"Datapoint sent successfully to {goal}!")
    else:
        print(f"Failed to send datapoint to {goal}:", response.text)


def button1_callback(channel):
    print("Button 1 pressed!")
    send_beeminder_datapoint(BEEMINDER_GOAL1)


def button2_callback(channel):
    print("Button 2 pressed!")
    send_beeminder_datapoint(BEEMINDER_GOAL2)


# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(BUTTON1_PIN, GPIO.FALLING, callback=button1_callback, bouncetime=1000)
GPIO.add_event_detect(BUTTON2_PIN, GPIO.FALLING, callback=button2_callback, bouncetime=1000)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
