import speech_recognition as sr
import pyttsx3
import webbrowser as wb
from musicfolder import music
import time
import pyautogui as pg

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop() 

def process_command(c):
    if "open google"  in c.lower():
        wb.open("https://google.com")
    elif "open youtube"  in c.lower():
        wb.open("https://youtube.com")
    elif "open instagram"  in c.lower():
        wb.open("https://instagram.com")    
    elif "open chatgpt"  in c.lower():
        wb.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= music[song]
        wb.open(link)
    elif "type" in c.lower():
        try:
            with sr.Microphone() as source:
                speak("Jarvis start typing...")
                audio=r.listen(source,timeout=1)
            text=r.recognize_google(audio)
            pg.write(text)

        except Exception as e:
            print("error",e)

if __name__ == "__main__":
    speak("Initializing jarvis...")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

            word = r.recognize_google(audio)
            print(word) 

            if word.lower() == "jarvis":
                speak("jarvis activated...")
                time.sleep(0.5)

                with sr.Microphone() as source:
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)

                command = r.recognize_google(audio)
                print(command)
                process_command(command)

        except Exception as e:
            print("Error:", e)
