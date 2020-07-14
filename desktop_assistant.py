import pyttsx3
import speech_recognition as sr 
import datetime
import os
import webbrowser
import sys
import subprocess as sp
import time
from time import strftime
import pyautogui
from tkinter import *
import playsound
try :
    def main():
        print("\n\n      ====>>  Welcome Back Sir  <<==== \n")
        print("\n ====>>  Iam Your Personal Assistant  <<==== \n\n")
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        volume = engine.getProperty('rate')
        engine.setProperty('rate',170)

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def wish_me():
            hour =int( datetime.datetime.now().hour)
            global wish
            if hour>=0 and hour < 12:
                wish = "Good Morning Sir"

            elif hour >=12 and hour<16:
                wish = "Good Afternoon Sir"
            
            else:
                wish = "Good Evening Sir"

            print(wish)
            speak(wish)
            
            time = strftime('%I : %M  %p')
            time2 = strftime('%I %M %p')
            print(f"Time is  {time}")
            speak(f"Time is {time2}")

            today = datetime.date.today()
            d2 = today.strftime("%B %d, %Y")
            print("Date Is ", d2)
            speak(f"Date Is {d2}")


        wish_me()

        print("Opening Google Chrome Is My Default Process.")
        os.startfile("www.google.com")
        speak("Opening Google Chrome Is My Default Process.")
        print("Now Iam Ready For Your Command Sir. Click On Help.")
        speak("Now Iam Ready For Your Command Sir. Click On Help")


        def takecommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("--Iam listening--")
                playsound.playsound('listen.mp3', True)
                audio = r.listen(source, phrase_time_limit=4)

            try:
                print("--Iam Recognizing...")
                # speak("Iam Recognizing...")
                global query
                query = r.recognize_google(audio)
                print(f"*** You told : {query} ***")
                
            except:
                print("Iam Unable To Recognise At This Moment. Please Try Again And Also Check Your Internet Connection.")
                speak("Iam Unable To Recognise At This Moment. Please Try Again And Also Check Your Internet Connection")
                query = None
            return query
            
        def what_can():
            
            print('you can ask this...')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url = "https://arshad272.github.io/whatcan.html"
            webbrowser.get(chrome_path).open(url)
            speak('you can ask this...')
            


        def perform():
            
            global query
            query = takecommand()

            try : 
                if 'open camera' in query.lower():
                    print("opening camera")
                    os.startfile('microsoft.windows.camera:')
                    speak("opening camera")
                    

                elif 'maps' in query.lower():
                    print("opening maps")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "https://www.google.com/maps/"
                    webbrowser.get(chrome_path).open(url)
                    speak("opening maps")
                    

                elif 'open youtube' in query.lower():
                    print("Opening youtube")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "youtube.com"
                    webbrowser.get(chrome_path).open(url)
                    speak("Opening Youtube")
                    

                elif 'open google' in query.lower():
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "google.com"
                    webbrowser.get(chrome_path).open(url)
                    cmdgoogle = takecommand()
                    pyautogui.write(cmdgoogle , interval=0.05)
                    pyautogui.press('enter')
                    

                elif 'open control panel' in query.lower():
                    os.system('control panel')
                    speak("opening control panel")
                    
                    
                elif 'open facebook' in query.lower():
                    print("Opening facebook")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "facebook.com"
                    webbrowser.get(chrome_path).open(url)
                    speak("Opening facebook")
                    

                elif 'open whatsapp' in query.lower():
                    print("Opening whatsapp")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "https://web.whatsapp.com/"
                    webbrowser.get(chrome_path).open(url)
                    speak("Opening whatsapp")            

                elif 'quran' in query.lower():
                    print("Playing Quran In Youtube")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "https://www.youtube.com/watch?v=963kSvgX7Zw"
                    webbrowser.get(chrome_path).open(url)
                    speak("Playing Quran In Youtube")
                
                elif 'open github' in query.lower():
                    print("Opening Github")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "https://github.com/"
                    webbrowser.get(chrome_path).open(url)
                    speak("Opening Github")
                

                elif 'open gmail' in query.lower():
                    print("Opening G Mail")
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "https://mail.google.com/mail/u/0/#inbox"
                    webbrowser.get(chrome_path).open(url)
                    speak("Opening G Mail")

                elif 'open notepad' in query.lower():
                    os.startfile("Notepad.exe")

                elif 'terminate' in query.lower():
                    print("See You Later Sir")
                    speak("See You Later Sir")
                    sys.exit()

                elif 'good night' in query.lower():
                    hour =int( datetime.datetime.now().hour)
                    
                    if hour>=20 :
                        speak("Good Night Sir.. Sweet Dreams... We Will Meet Later")
                        print("Good Night Sir.. Sweet Dreams... We Will Meet Later")

                    else:
                        print("Ohh No. Its day time Sir...")
                        speak("Ohh No. Its day time Sir...")
                        
                    
                elif 'what can you' in query.lower():
                    what_can()

                elif 'how are you' in query.lower():
                    print("I am fine. What about you Sir ? ")
                    speak("I am fine. What about you Sir ")
                    query8 = takecommand()
                    
                    if 'not' or 'bad' or 'worse' or 'stress' in query8.lower():
                        print('Its okk..')
                        speak("its ok...")

                    else:
                        print("Its Ok... ")
                        speak("Its Ok")
                    print("How can I help you ?")
                    speak("How can I help you ")
                    perform()

                elif 'open' in query.lower():
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "google.com"
                    webbrowser.get(chrome_path).open(url)
                    time.sleep(2)
                    pyautogui.write(query , interval=0.05)
                    pyautogui.press('enter')
                    print("Trying To Open Sir.")
                    speak("Trying To Open Sir.")
                    
                
                elif 'tell me' or 'what is' or 'who is' or 'how to' or 'know' in query.lower():
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    url = "google.com"
                    webbrowser.get(chrome_path).open(url)
                    time.sleep(2)
                    pyautogui.write(query , interval=0.05)
                    pyautogui.press('enter')
                    print("I Found This Sir. ")
                    speak("I Found This Sir. ")
                    

                else:
                    webbrowser.open(query)
            
            except :
                pass


        window = Tk()

        window.title("Desktop Assistant")
        window.iconbitmap('perfect3.ico')
        label = Label(window, text=wish+"\nIam your personal assistant\nArshad Created Me \nPlease Click on Help",
                    font=("Times New Roman", 20), bg='black', fg='white')
        label.pack()
        # imagetest = PhotoImage(file="icons\\pngicon.png")

        btn = Button(window, text = "Help",bg='blue',fg='white',activeforeground='white',activebackground='green',font=('Helvetica', '15'),compound = LEFT,command = perform)
        btn.pack(side = LEFT, fill = X, expand=YES)
        def dstry():
            print("Byee... We Will meet later")
            speak("Terminating Virtual Desktop Assistant")
            window.destroy()
        btn1 = Button(window, text = "Exit",bg='red',fg='white',activeforeground='white',activebackground='green',font=('Helvetica', '15'),command = dstry)
        btn1.pack(expand=YES, fill = X, side=LEFT)

        window.mainloop()

except ModuleNotFoundError:
    print("First Install All Required Modules : ")
    print("pip install pyttsx3 \npip install pyautogui \npip install playsound \npip install speechRecognition")
