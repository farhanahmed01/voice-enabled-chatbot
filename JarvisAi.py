import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import time
import pandas as pd
import playsound as play
import os
import pyjokes 
import cv
import pyautogui
import numpy as np
import random
import pywhatkit as kit
import math
import time
import requests
import tkinter as tk

engine = pyttsx3.init()
voice = engine.getProperty('voice')
# print(voices[1].id)
engine.setProperty('voice', voice[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime ("%I:%M:%p")
    if hour>=0 and hour<12:
        print(f"Good Morning! sir, its {tt}")
        speak(f"Good Morning! sir, its ,,{tt}")
        

    elif hour>=12 and hour<18:
        print(f"Good Afternoon! sir,its {tt}") 
        speak(f"Good Afternoon! sir,its {tt}")  
        
    else:
        print(f"Good Evening! sir,its {tt}")
        speak(f"Good Evening! sir,its {tt}")  

       
    print("please tell me how may i help you")
    speak("Please tell me how may I help you")  
        

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="c20b1a39fb3e47dcbda859ec8181ec83"'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new("https://youtube.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'close google' in  query :
            speak("closing google")
            

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com")   


        elif 'play music on spotify' in query:
            speak ("playing sond on spotify ")
            webbrowser.open("https://open.spotify.com/playlist/2c4agrVbHnEET0WOw2sK0K")

        ##elif 'send message' in query:
          
          
          ##  s=str(input("enter the message"))
            ##kit.sendwhatmsg('+919711539373', s ,1,51)
            ##time.sleep(10)
            ##speak("message has been sent")
            #3print("message has been sent")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'hello jarvis' in  query :
            speak("hello sir how r you") 

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "farhanahmed20033@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend farhan bhai. I am not able to send this email")    

        elif 'sleep jarvis' in query :
            speak("good bye sir")
            print ("good bye sir")
            exit()

        elif 'hola' in query :
            speak("hello everybody i am an advance A P I, and my name is jarvis")
        
        elif 'song' in  query :
            music_dir = '/Users/farhanahmed/Documents/song'
            songs= os.listdir(music_dir)
            print(songs)
            os.starfile(os.path.join(music_dir , songs[1]))
            

        elif 'is been too late today' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" yes Sir, the time is {strTime} now so please go and ")
            speak ("take rest")
        
        elif 'okay jarvis' in query:
            speak("then good night sir and have a good sleep")

        elif 'tell me a joke ' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'how are you' in query:
            speak("I an good sir , And what about you sir.")

        elif "i am good " in query:
            speak("that's sound's great sir , Tell me sir how may i help you ")

        elif "tell me news" in query:
            speak("news are you serious, you are saying about news")
            

        elif "shut up jarvis tell me the news" in query:
            speak("okay sir , fetching the latest news for you")
            news()

        elif 'switch the window' in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("tab")
            time.sleep(4)
            pyautogui.keyUp("ctrl")

        elif "start a game" in query:
            print("1.choose number between any range")
            print("2.flip a coin")
            print("3.roll a dice")
            speak("1.choose number between any range")
            speak("2.flip a coin")
            speak("3.roll a dice")

            answer=int(input("enter the option\n"))
            if answer==1:
                speak("the game is about to start")
                print("the game is about to start\n")
                
                def Rand(start, end, num):
                    res = []
                    for j in range(num):
                        res.append(random.randint(start, end))
                    return res
                speak("enter the digit")
                num = int(input("enter the digit"))
                speak("enter the starting limit")
                start = int(input("enter the starting limit"))
                speak("enter the ending limit")
                end = int(input("enter the ending limit"))
                s=print(Rand(start, end, num))

            elif answer==2:
                speak("Now to we gonna play a game in which one coin is tosssed")
                print("the game is about to start\n")

                def cointoss():
                     rand_i = random.randint(0, 1)
                     outcomes = ["Heads", "Tails"]
                     return outcomes[rand_i]
                t1 = cointoss()
                ##t2 = cointoss()
                ##t3 = cointoss()
                print(t1)

            elif answer==3:
                speak("Now we are going to play an intresting game in which a dice is rolled and the random number popes out")
                print("the game is about to start\n")

                min = 1
                max = 6
                # Setting the default value of flag to yes.
                Flag = "yes"
                while Flag == "yes" or Flag == "y":
                    print("Now Rolling the dice...")
                    print ("Number on the dice is: ")
                    print(random.randint(min, max))
                    Flag = input("Are you interested to Roll the dice again? ")

        elif "play video on youtube" in query:
            kit.playonyt("Taarak Mehta Ka Ooltah Chashmah - Episode 384")

        elif "start unit conversion" in query:
            
            speak("Which category would you like to convert? :  ")
            cat = input ("Which category would you like to convert? :  ")
            if cat == ("l"):
                Flag = "yes"
                while Flag == "yes" or Flag == "y":
                    speak("the conversions available are")
                    print("The conversions available are")
                    print("1.cm to m")
                    print("2.mm to cm")
                    print("3.m to cm")
                    print("4.cm to mm")
                    print("5.mm to m")
                    print("6.m to mm")
                    print("7.km to m")
                    print("8.m to km")
                    print("9.mm to km")
                    speak("1.cm to m")
                    speak("2.mm to cm")
                    speak("3.m to cm")
                    speak("4.cm to mm")
                    speak("5.mm to m")
                    speak("6.m to mm")
                    speak("7.km to m")
                    speak("8.m to km")
                    speak("9.mm to km")
                    speak("Which unit would you like to convert from: ")
                    unit1 = input ("Which unit would you like to convert from: ")
                    speak("Which unit would you like to convert to: ")
                    unit2 = input ("Which unit would you like to convert to: ")
                    speak("Enter your value:")
                    num1 = int(input ("Enter your value: " ))
                    if unit1 == "cm" and unit2 == "m":
                        ans = float(num1)/100
                        print(ans)  
                    elif unit1 == "mm" and unit2 == "cm":
                        ans = float(num1)/10
                        print(ans)
                    elif unit1 == "m" and unit2 == "cm":
                        ans = float(num1)*100
                        print(ans)
                    elif unit1 == "cm" and unit2 == "mm":
                        ans = float(num1)*10
                        print(ans)
                    elif unit1 == "mm" and unit2 == "m":
                        ans = float(num1)/1000
                        print(ans)
                    elif unit1 == "m" and unit2 == "mm":
                        ans = float(num1)*1000
                        print(ans)
                    elif unit1 == "km" and unit2 == "m":
                        ans = float(num1)*1000
                        print(ans)
                    elif unit1 == "m" and unit2 == "km":
                        ans = float(num1)/1000
                        print(ans)
                    elif unit1 == "mm" and unit2 == "km":
                        ans = float(num1)/1000000 
                        print(ans)
                    Flag = input("Are you interested to do again? ")

        elif "make a note" in query:
            speak("what i have to note sir!.")
            def create_note () : 
                global recognizer
                engine. say ("What do you want to write onto your note?") 
                engine .runAndWait()
                done = False 
                while not done:
                    try: 
                        with sr.Microphone() as mic: 
                            recognizer.adjust_for_ambient_noise (mic, duration=0.2) 
                            audio = recognizer.listen(mic)
                            note = recognizer.recognize_google (audio)
                            note = note. lower ()
                        engine. say ("Choose a filename!") 
                        engine. runAndWait () 
                        recognizer .adjust_for_ambient_noise(mic, duration=0.2) 
                        audio = recognizer. listen (mic)
                        filename = recognizer .recognize_google (audio)
                        filename = filename. Lower ()
                        with open (filename, 'w') as f: 
                            f.write(note)
                            done = True 
                            engine. say (f"I successfully created the note {filename}") 
                            engine.runAndWait() 

                    except sr. UnknownValueError: 
                        recognizer = sr.Recognizer() 
                        engine. say ("I did not understand you! Please try again")
                        engine.runAndWait() 

        
        elif "calculation" in query:
            speak("the calculations available are")
            print("1.addition")
            print("2.substraction")
            print("3.multiplication")
            print("4.division")
            speak("1.addition")
            speak("2.substraction")
            speak("3.multiplication")
            speak("4.division")

            a=int(input("enter the option"))
            if a == 1:
                def SumOfNNums(arr, tot):
                    s = 0
                    for i in range(tot):
                        s = s+arr[i]
                    return s

                num = []
                print(end="Enter the Value of n: ")
                n = int(input())
                print(end="Enter " + str(n) + " Numbers: ")
                for i in range(n):
                    num.insert(i, int(input()))

                sum = SumOfNNums(num, n)
                print("\nSum of " + str(n) + " Numbers = " + str(sum))

            elif a==2:
                def SumOfNNums(arr, tot):
                    s = 0
                    for i in range(tot):
                        s = s+arr[i]
                    return s

                num = []
                print(end="Enter the Value of n: ")
                n = int(input())
                print(end="Enter " - str(n) - " Numbers: ")
                for i in range(n):
                    num.insert(i, int(input()))

                sum = SumOfNNums(num, n)
                print("\nSum of " - str(n) - " Numbers = " + str(sum))