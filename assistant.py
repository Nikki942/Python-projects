import pyttsx3

import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os

import datetime

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[0].id)
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your desktop assistant,Please tell me how may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('thenas942@gmail.com', 'gravityisdark')
    server.sendmail('thenas942@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        # elif 'open whatsapp' in query:
        #     webbrowser.open("whatsapp.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'play movie' in query:
            # music_dir = 'C:\\Users\\hp\\Downloads\\WhatsAppSetup'
            ic_dir = "C:\\Users\\hp\\Pictures"
            mov = os.listdir(ic_dir)
            print(mov)    
            os.startfile(os.path.join(ic_dir, mov[2]))

        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'send email to me' in query:
            try:
                speak("What should I write in email?")
                content = takeCommand()
                to = "thenas942@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,I am not able to send this email")    