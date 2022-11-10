import datetime
import webbrowser
import threading
import center_tk_window
# import pyjokes
# from quote import quote
from tkinter import *
import pyttsx3
import pywhatkit as kit
import googlesearch
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
time = datetime.datetime.now()
time.hour



# Pysist = Tk()
# Pysist.title("Pysist")
# Pysist.maxsize(2000, 800),

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    #window.after(1000)
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening....")
        T.insert(END, "Listening...." + "\n\n")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            T.insert(END, "Recognizing...."+"\n\n")
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            T.insert(END, f"Amigo: ", query + "\n\n")
            print(f"User said: ", query)
        except Exception as e:
            T.insert(END, "Say that again \n\n")
            print("Say that again")
            return "None"
        return query


# def start():
#     query = command().lower()
#     if query =="pysist":
#         op()
def window():
    global window
    window = Tk()
    window.title("AMIGO")
    #window.config(bg="white")
    window.minsize(1000, 800)
    img = PhotoImage(file="C:/Users/aayush/Downloads/amigo.png")
    l1 = Label(window, image=img, bg="white")
    l1.pack()
    window.config(bg="white")
    #img1 = PhotoImage(file="C:/Users/aayush/Downloads/mic1.png")
    # img1= img1.resize(width=100, height=50)
    b = Button(window, command=threading.Thread(target=op, daemon=True).start())
    #b.place(x=480, y=600)
    window.iconbitmap("C:/Users/aayush/Downloads/logo1.ico")
    global T
    T = Text(window, height=24, width=100, bg="white")
    T.place(x=0, y=200)
    T.configure(font="ComicSansMS")
    # b = Button(window, text="Mic", width=20, height=34)
    # b.pack()
    sb = Scrollbar(window)
    sb.pack(side=RIGHT, fill=Y)
    T.config(yscrollcommand=sb.set)
    sb.config(command=T.yview(END), wrap=WORD)
    T.tag_configure("center", justify='center')
    T.tag_add("center", 0.1, "end")
    T.pack()
    window.mainloop()
    # window.minsize(100, 200)

def greet():
    # l4 = Label(window, text="Hello, I am your Amigo", font=("Times New Roman", 18))
    # l4.pack()
    T.insert(END, "Hello, I am your Amigo"+"\n\n")
    speak("Hello, I am your Amigo")
    T.insert(END, "What is Your Name?"+"\n\n")
    speak("What is Your Name")
    query = command().lower()
    T.insert(END, "Heyy "+query+"\n\n")
    speak("Heyy" + query)
    if time.hour < 12:
        print("good morning")
        T.insert(END, "Good Morning"+"\n\n")
        speak("Good Morning")
    if time.hour >= 12 and time.hour < 18:
        print("good afternoon")
        T.insert(END, "Good Afternoon"+"\n\n")
        speak("Good afternoon")
    if time.hour >= 18 and time.hour < 22:
        print("good evening")
        T.insert(END, "Good Evening"+"\n\n")
        speak("Good Evening")
    # l4.destroy()
    # l5.destroy()
    # l6.destroy()
    # l7.destroy()
    op()


def op():
    while True:
        query = command().lower()
        if query == "amigo":
            T.insert(END, "How May I help you"+"\n\n")
            speak("How May I help you")
            query = command().lower()
            if 'youtube' in query:
                # l8 = Label(window, text="Which Song", font=("Times New Roman", 18))
                # l8.pack()
                T.insert(END, "Which Song" + "\n\n")
                speak("Which song")
                query = command().lower()
                T.insert(END, "Playing " + query + "\n\n")
                kit.playonyt(query)
                speak("Here is the result")
            elif 'google' in query:
                T.insert(END, "What to search \n\n")
                speak("What to search")
                query = command().lower()
                T.insert(END, query + "\n\n")
                webbrowser.open("https://www.google.com/search?q=" + query + "&rlz=1C1FHFK_enIN931IN931&oq=" + query + "&aqs=chrome.0.0i355i433i512j46i433i512j69i59j0i512j46i131i433j69i60j69i61j69i60.2820j0j4&sourceid=chrome&ie=UTF-8")
                # query = r.recognize_google("")
                speak("Here are the results")
            elif 'hello' in query:
                greet()
            elif "good morning" in query:
                if time.hour < 12:
                    print("good morning")
                    T.insert(END, "Good Morning" + "\n\n")
                    speak("Good Morning")
                else:
                    print("its not morning")
                    speak("its not morning")
            elif "good aftenoon" in query:
                if time.hour >= 12 and time.hour < 18:
                    print("good afternoon")
                    T.insert(END, "Good Afternoon" + "\n\n")
                    speak("Good afternoon")
                else:
                    print("its not afternoon")
                    speak("its not afternoon")
            elif "good evening" in query:
                if time.hour >= 18 and time.hour < 22:
                    print("good evening")
                    T.insert(END, "Good Evening" + "\n\n")
                    speak("Good Evening")
                else:
                    print("its not evening")
                    speak("its not evening")
            # elif 'joke' in query:
            #     engine.setProperty('rate', 140)
            #     joke = pyjokes.get_joke(language="en", category="neutral")
            #     print(joke)
            #     T.insert(END, joke + "\n\n")
            #     speak(joke)
            elif "good night" in query:
                print("Good night")
                T.insert(END, "Good Night" + "\n\n")
                speak("Good night")
            # elif 'good saying' in query:
            #     engine.setProperty('rate', 140)
            #     q = quote('family', 2)
            #     print(q)
            #     T.insert(END, quote + "\n\n")
            #     speak(q)
            elif "stop" in query:
                break
            else:
                print("Didn't get it")
                T.insert(END, "Didn't get it" + "\n\n")
                speak("Didn't get it")
                print("Please say it again")
                T.insert(END, "Please say it again" + "\n\n")
                speak("Please say it again")
                op()
            #l8.destroy()
    # elif 'stop' in query:


if __name__ == '__main__':
    window()
# def talk(text):
#     speech.say(text)
#     speech.runAndWait()
