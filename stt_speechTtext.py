import speech_recognition as sr

listner= sr.Recognizer()

def record_text(torec):
    while(torec):
        try:
            with sr.Microphone() as source2:
                print("SPEAK ")
                listner.adjust_for_ambient_noise(source2, duration=0.1)
                audio= listner.listen(source2)
                text= listner.recognize_whisper(audio,language='en')
                return text

        except sr.RequestError as e:
            print("could not requests results {}".format(e))

        except sr.UnknownValueError as e:
            print("could not requests results {}".format(e))
    return

def outputText(text):
    print(text)
    return



