import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

#removed now as i only needed this to get the voice ID
#print(voices)
#print(voices[0])
#print(voices[1])

engine.setProperty('voice', voices[1].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

