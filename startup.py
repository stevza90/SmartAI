import speech
import responces


def startup_speech():
    print("Playing start up speech")
    speech.speak(".")
    responces.responces()