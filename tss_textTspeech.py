import pyttsx3

speaker= pyttsx3.init()

def Speak(text):
    speaker.say(text)
    speaker.runAndWait()

# Speak("how are you my friend?")