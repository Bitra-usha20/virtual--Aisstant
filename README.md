overview

This Python script is a **voice assistant** program that:

* Listens to your voice commands
* Responds with speech using `pyttsx3`
* Performs tasks like telling time/date, opening Notepad, YouTube, or searching on Google.

It uses **speech recognition + text-to-speech + OS/web integration**.

---

## 📂 **Breakdown of the Code**

### 1. **Imports**

```python
import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyaudio
from datetime import datetime
```

* `os` → Run system commands (like opening Notepad).
* `datetime` → Get current date and time.
* `pyttsx3` → Text-to-speech engine (speaks back to you).
* `speech_recognition` (`sr`) → Recognizes your speech through a microphone.
* `webbrowser` → Opens websites.
* `pyaudio` → Required for microphone input.

---

### 2. **Text-to-Speech Setup**

```python
engine = pyttsx3.init()
engine.setProperty('rate', 175)
```

* Initializes the voice engine.
* `rate=175` → Controls speaking speed.

---

### 3. **Speak Function**

```python
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
```

* Converts text → speech.
* Also prints the response on the console.

---

### 4. **Listening for Commands**

```python
def take_command():
    listner = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        audio = listner.listen(source)
        try:
            command = listner.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
        except:
            return ""
```

* Uses the microphone to listen.
* Google Speech Recognition converts **audio → text**.
* Converts command to lowercase for easier matching.
* If it fails, returns an empty string.

---

### 5. **Assistant Logic**

```python
def run_assistant():
    command = take_command()
```

Checks the user’s command and responds accordingly:

* **Time**

```python
if "time" in command:
    time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")


✅ Says current time (e.g., "The current time is 04:30 PM").

* **Date**

python code
elif "date" in command:
    date = datetime.today()
    speak(f"Today's date is {date}")

✅ Says today’s date (full format with year, month, day, etc.).

* **Open Notepad**

python code
elif "open notepad" in command:
    os.system('notepad')


✅ Opens Notepad on Windows.

* **Open YouTube**

python code
elif "open youtube" in command:
    webbrowser.open("https://www.youtube.com/")


✅ Opens YouTube in default browser.

* **Google Search with "hey siri"**

python code
elif "hey siri" in command:
    query = command.replace("hey siri", "")
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)


✅ Example: If you say `"hey siri python tutorial"`, it searches Google for *python tutorial*.

* **Exit / Stop**
python code
elif "bye" in command or "stop" in command:
    speak("Okay thank you, you may leave")
    exit()

✅ Ends the program.

* **Fallback (Default Reply)**

```python
else:
    speak("I am here to assist you. Like open YouTube or Notepad, or tell you time and date.")
```

✅ If it doesn’t understand, it gives a generic response.

---

### 6. **Main Function**

```python
if __name__ == "__main__":
    speak("Hey Buddy! Hi, I am here to assist you...")
    while True:
        run_assistant()

* Starts with a greeting.
* Runs in an infinite loop → keeps listening until you say `"bye"` or `"stop"`.


**What This Assistant Can Do**

1. Speak responses (text-to-speech).
2. Listen to your voice commands.
3. Tell you the **current time and date**.
4. Open **Notepad**.
5. Open **YouTube**.
6. Perform a **Google search** when you say `"hey siri <query>"`.
7. Exit when you say `"bye"` or `"stop".
