import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import cv2
from requests import get
import requests
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import instaloader
import PyPDF2
import operator
import time
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import MyAlarm





engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#text to speech...
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish....
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Ohhh Hello sir, Jarvis here, Please tell me how may I help you.")


def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       # print(e)
        print("say that again please...")
        return"None"
    return query
#for news
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ae419b8db8b24d0cbaf433f028de1fe2'

    
    main_page = get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day =["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","teeth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is:", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

#pdf reader....
def pdf_reader():
    book =open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of the pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text) 

def TaskExecution():
    wishMe()
    while True:
    #if 1:
        
        query = takeCommand().lower()

        # logic for executing tasks based query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()           
            url = f"https://www.google.com/search?q={cm}"
            webbrowser.open(f"{url}")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            speak("opening sir, and remember sir please do not spend much time on it")
            webbrowser.open("instagram.com")

        
        
        elif 'open news' in query:
            webbrowser.open("news.com")

        elif 'play music' in query or 'open music' in query or 'play song' in query:
            speak("which type music or song you want to listen sir ? ")
            cm =takeCommand().lower()
            song = cm.replace('play','')

            kit.playonyt(song)

           # url = f"https://www.youtube.com/search?q={cm}"
           # webbrowser.open(f"{url}")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open github' in query or 'github' in query:
            webbrowser.open("https://github.com/")

        

        elif 'the time' in query or 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open notepad' in query:
            nPath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(nPath)



        elif 'open command prompt' in query:
            os.system("start cmd")


        elif 'shut down the system' in query or 'shutdown the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")


        elif 'put you in sleep mode' in query or 'on sleep mode' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        elif 'close notepad' in query:
            speak("ok sir, i am closing it")
            os.system("taskill /f /im notepad.exe")

        elif 'close code' in query:
            speak("ok sir, i am closing it")
            os.system("taskill /f /im code.exe")



        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")


#....for calculation......

        elif 'do some calculation' in query or 'can you calculate' in query or 'on calculator' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what yo want to calculate")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add, #plus
                    '-' : operator.sub, #minus
                    '*' : operator.mul, #multiplied
                    'divided' :operator.__truediv__, #division
                }[op]
            def eval_binary_expr(op1, oper, op2): #5 plus 8
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
        
        #to find my location :
        elif 'where i am' in query or 'where we are' in query:
            speak("wait sir, let me check")

            main = requests.get('https://ipinfo.io/').json()
            loci = main ['loc'].split(',')
            lat = float(loci[0])
            long = float(loci[1])
            speak("sorry sir for the delay we have a slow internet connection.")
            speak(f"your latitude is {lat} and your longitude is {long}")


#to check instagram profile:
        elif 'check instagram profile' in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            speak("sir would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder.now i am ready for your next command.")
            else:
                pass

# to  take screenshot ...........
        elif 'take screenshot' in query or 'take a screenshot' in query or 'screenshot' in query:
            speak("sir, Please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our folder.now i am ready for the next command")
            
# for weather forcast...

        elif 'temperature' in query :
            search = "today's temperature in my location"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data =BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

#how to do mode....

        elif 'activate how to do mode' in query or 'on how to do mode' in query:
            speak("How to do mode is activated.")
            while True:
                speak("Please tell me what you want to know")
                how = takeCommand().lower()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this.")

     #check battery status.....

        elif 'how much power left' in query or 'how much power we have' in query or 'battery'  in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=45 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentage<=15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")
                     

        elif 'alarm' in query:
            speak("sir please tell me the time to set alarm")
            tt = takeCommand().lower()
            tt = tt.replace("set alarm to ", "")#5:30 am
            tt = tt.replace(".","")
            tt = tt.upper()
            
            MyAlarm.alarm(tt)

#for volume control....

        elif 'volume up' in query or 'increase the volume' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query or 'decrease the volume' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query or 'mute the volume' in query:
            pyautogui.press("volumemute")



        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k =cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()



        elif 'send message' in query:
            kit.sendwhatmsg("+917294878246", "hey" ,9,22)


        elif 'tell me a joke' in query: 
            joke = pyjokes.get_joke()
            speak(joke)


        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        
        elif 'tell me news' in query:
            speak("please wait sir, feteching the latest news")
            news() 

        #......to read pdf file.....

        elif 'read PDF' in query:
            pdf_reader()

        elif 'hello' in query or 'hey' in query:
            speak("hello sir, may i help you with something.")

        elif 'how are you jarvis' in query:
            speak("Doing well sir ,what about you.")

        elif 'i am fine' in query or 'i am also good' in query or 'fine' in query or 'i am also doing well' in query:
            speak("That's great to hear from you.")
         
        elif 'thank you jarvis' in query or 'thanks' in query or 'thank you' in query:
            speak("It's my pleasure sir, any other work for me sir?")

        elif 'no thanks' in query or 'you can sleep now' in query:
            speak("Got it sir, i am going to sleep you can call me anytime.")
            break

        elif 'good bye jarvis' in query or 'good bye' in query or 'goodbye jarvis' in query or 'gooodbye' in query:
            speak("Thanks for using me sir ,have a good day to you")
            sys.exit()
    
   


if __name__ == "__main__":
    while True:
        permission = takeCommand().lower()
        if "wake up" in permission or "wake up jarvis" in permission or " jarvis are you there" in permission :
            TaskExecution()
        
        
    

   

        

        


    
    