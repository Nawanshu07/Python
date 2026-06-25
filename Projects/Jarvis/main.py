import speech_recognition as sr
import pyttsx3
import webbrowser



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open insta" in command.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    r =sr.Recognizer()
    while True:
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=5 , phrase_time_limit=5)
            print("Recognising......")
            command = r.recognize_google(audio).lower().strip()
            print(command)
            
            if "jarvis" in command.lower():
                print("JARVIS DETECTED!")
                speak("yeah")
                
                with sr.Microphone() as source:
                    print("Jarvis is activated!")
                    audio = r.listen(source)
                print("Recognising......")
                command = r.recognize_google(audio)
                process_command(command)


        except sr.UnknownValueError:
            print("I don't understand what you said?")
        except Exception as e:
            print(e)