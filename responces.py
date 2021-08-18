import speech
import end
import datetime
import os
import calculator
import repeat
import webbrowser
import ofage

def responces():
    speech.speak("Enter your name: ")
    name = input("Enter your name: ")
    speech.speak("Hello " + name)
    speech.speak("What is your age")
    age = input("What is your age?: ")
    age = int(age)

    running = True

    while (running == True):
        speech.speak("Listening? ")
        command = input("What do you want to do? ")
        command = command.upper()

        speech.speak = speech.speak
        if command == "TIME":
            speech.speak("The time is now!")
            speech.speak(datetime.datetime.now().hour)
            speech.speak(datetime.datetime.now().minute)

        elif command == 'AGE':
            speech.speak("You told me your age was " +age)

        elif command == "DATE":
            speech.speak(datetime.datetime.now().date())

        elif command == "WHAT":
            speech.speak("I am not repeating myself")

        elif command == "BYE" :
            speech.speak("Well fuck you then")

        elif command == "CHANGE MY NAME":
            speech.speak("Enter your new name: ")
            name = input("Enter your new name! ")
            speech.speak("Named changed successfully to: " + name)
            print("Named changed successfully to: " + name)

        elif command == "MY NAME":
            print("You told me your name was: " +name)
            speech.speak("You told me your name was " + name)

        elif command == "CONTROL":
            os.system('control')

        elif command == "SHUTDOWN":
            os.system("shutdown -s -t 0")

        elif command == "EXIT" :
            speech.speak("Good Bye!")
            end.end_program()

        elif command == 'CMD':
            os.system('cmd')

        elif command == "HELLO":
            speech.speak("Hello " + name)

        elif command == "CALCULATOR":
            speech.speak("Starting Calulator")
            calculator.calculator()

        elif command == "FUCK YOU" and age >= 18:
            ofage.fuckYou()

        elif command == "ECHO" :
            print(command + " Was all in upper case")
            speech.speak(command + ", WAS all in upper case")

        elif command == "REPEAT" :
            repeat.repeat()

        elif command == 'COMMAND' :
            os.system('cmd')

        elif command == 'DOCUMENTATION' :
            speech.speak('To get all my information you can visit, www.stephenwilde.net/alpha34')

        elif command == "I WANT TO DIE" or command == 'HOW DO I KILL MYSELF' or command == 'EASY WAYS TO DIE' :
            webbrowser.open('https://www.google.com/search?q=suicide+prevention', new=2)
            speech.speak("You are not alone, here is some help!")
            #t = 2
            #time.sleep(t)

        elif command == "TWAT" and age >= 18:
            ofage.twat()

        else:
            speech.speak("Not recognised - Please try again")