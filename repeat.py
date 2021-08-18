import speech


def repeat() :
    speech.speak("What do you want me to repeat")
    repeat = input("What do you want me to repeat: ")
    speech.speak(repeat)
    speech.speak('Do you want me to repeat something else, Y, N')
    yn()

def yn() :
    yesno = input("Do you want me to repeat something else (y/n): ")
    yesno = yesno.upper()

    if yesno == 'Y':
        repeat()
