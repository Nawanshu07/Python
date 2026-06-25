import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command:str):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")

    elif "open insta" in command.lower():
        webbrowser.open("https://instagram.com")

    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
        
    elif command.lower().startswith("play"):
        song = command.strip().lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    r =sr.Recognizer()
    while True:
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=5 , phrase_time_limit=5)
            command = r.recognize_google(audio).lower().strip()
            print(command)
            
            if "jarvis" in command.lower():
                speak("yeah")
                
                with sr.Microphone() as source:
                    print("Jarvis is activated!")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                process_command(command)


        except sr.UnknownValueError:
            print("I don't understand what you said?")
        except Exception as e:
            print(e)