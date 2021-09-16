# Imports
import pyttsx3
import random

# Variables
compliments = ["You look nice", "I think you are ok", "You have a nice head", "You have nice hair", "You look like a nice person", "You are ok"]
c = 0


# While Loop
while c <= 100000000000000:
    # Start-up
    engine = pyttsx3.init()

    # voices
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)

    # Talking
    engine.say(random.choice(compliments))
    engine.runAndWait()

    c = c + 1
