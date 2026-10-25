import speech_recognition as sr
import pyttsx3
import webbrowser as wb
from musicfolder import music
import pyautogui as pg

active = False

engine = pyttsx3.init()
r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def process_command(c):

    if "open google" in c.lower():
        wb.open("https://google.com")

    elif "open youtube" in c.lower():
        wb.open("https://youtube.com")

    elif "open instagram" in c.lower():
        wb.open("https://instagram.com")

    elif "open chatgpt" in c.lower():
        wb.open("https://chatgpt.com")

    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()

        if song in music:
            wb.open(music[song])
        else:
            speak("Song not found.")

    elif "start typing" in c.lower():

        speak("What should I type?")

        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5, phrase_time_limit=30)

        text = r.recognize_google(audio)

        pg.write(text, interval=0.03)

        speak("Done typing.")


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        try:

            with sr.Microphone() as source:

                print("Listening...")
                audio = r.listen(source)

            word = r.recognize_google(audio).lower()

            print(word)

            if active == False:

                if "jarvis" in word:
                    active = True
                    print("jarvis activated...")
                    speak("Jarvis activated....")

            else:

                if "sleep" in word:
                    active = False
                    speak("Jarvis is in sleep mode...")

                else:
                    process_command(word)

        except Exception as e:
            print("Error:", e)