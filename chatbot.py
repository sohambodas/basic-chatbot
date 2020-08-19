import os
import pyttsx3

#choices in the form of menu
menu = ['notepad', 'chrome', 'wmplayer', 'paint']
pyttsx3.speak("choose a program from the list below:")
for i in menu:
    print(i)

#keywords in the form of lists

start = ['start','begin','launch', 'open', 'play', 'run']

npad = ['notepad','note pad', 'text editor', 'texteditor','editor']

chrome = ['browser','chrome','web browser','webbrowser','google','google chrome']

paint = ['paint','ms paint', 'mspaint','scratch book','drawing']

wmp = ['wmplayer','wmp', 'music player','musicplayer','music','media player','mesiaplayer']

negative = ['not ', 'dont',"don't", 'no ']

quit = ['end','stop','finish', 'quit', 'over']


while(True):
    pyttsx3.speak("enter your request:")
    text = input("your request: ")
    text = text.lower()
    if any(word in text for word in quit) and not(any(word in text for word in negative)):
        pyttsx3.speak("thank you for using our service!!")
        break;
    elif any(word in text for word in start) and any(word in text for word in npad) and not(any(word in text for word in negative)):
        print("Notepad is running...")
        pyttsx3.speak("Notepad is started...")
        os.system("notepad")
    elif any(word in text for word in start) and any(word in text for word in chrome) and not(any(word in text for word in negative)):
        print("Chrome is running...")
        pyttsx3.speak("Chrome is started...")
        os.system("chrome")
    elif any(word in text for word in start) and any(word in text for word in paint) and not(any(word in text for word in negative)):
        print("Paint is running...")
        pyttsx3.speak("Paint is started...")
        os.system("Paint")
    elif any(word in text for word in start) and any(word in text for word in wmp) and not(any(word in text for word in negative)):
        print("Media Player is running...")
        pyttsx3.speak("Media Player is started...")
        os.system("wmplayer")
    elif any(word in text for word in negative):
        pass
    else:
        pyttsx3.speak("Sorry!! i did not understand you, try again...")

