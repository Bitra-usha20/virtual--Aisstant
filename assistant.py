import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyaudio
from datetime import datetime



#create engine for text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 175)

#speak function you have to create
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    pass


#command taking function
def take_command():
    listner = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        audio = listner.listen(source)
        try:
            command = listner.recognize_google(audio)  # audio to text format
            command = command.lower()  # used to convert to lower
            print("You said:", command)
            return command
        except:
            return ""
        
#run assistant
def run_assistant():
    command = take_command()
    # in command it have time word
    if "time" in command:
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    # date in command , it returns the current date
    elif "date" in command:
        date = datetime.today()
        speak(f"Today's date is {date}")
    # open notepad command
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system('notepad')  # used to open the notepad

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    # search for any query
    elif "hey siri" in command:
        query = command.replace("hey siri", "")
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Looking for {query}")
            webbrowser.open(url)
    elif "bye" in command or "stop" in command:
        speak("Okay thank you, you may leave")
        exit()
    else:
        speak("I am here to assist you. Like open YouTube or Notepad, or tell you time and date.")
        

#main function
if __name__ == "__main__":
    speak("Hey Buddy! Hi, I am here to assist you to open YouTube or Notepad, say time and date, or ask any query.")
    while True:
        run_assistant()
