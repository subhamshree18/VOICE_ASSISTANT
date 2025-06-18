import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Please say it again.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def run_assistant():
    wish_user()
    while True:
        command = take_command()

        if 'hello' in command:
            speak("Hello! How are you?")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            speak(f"Today's date is {date}")
        elif 'search' in command:
            topic = command.replace('search', '')
            speak(f"Searching for {topic}")
            pywhatkit.search(topic)
        elif 'stop' in command or 'bye' in command:
            speak("Goodbye! Have a great day.")
            break
        elif command != "":
            speak("Sorry, I can’t do that yet.")


run_assistant()
