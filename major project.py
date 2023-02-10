import tkinter
from tkinter import *
from tkinter import ttk
import pyttsx3
from tkinter import filedialog
from path import Path
import speech_recognition as sr
from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment
import os
from time import sleep

def takeCommand():
    global showText, go, command
    showText.delete(1.0, "end")
    showText.insert(END, "Listening....")
    e = ["en-IN","te-IN","hi-IN","mr-IN","ur-IN","ta-IN","ml-IN","kn-IN","bn-IN","pa-IN"]

    recog = sr.Recognizer()
    command = ''

    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language=e[n])
        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"


def stop():
    global go, command
    print("q pressed, exiting...")
    go = 0
    showText.delete(1.0, "end")
    showText.insert(END, command)
def togetind():
    global n
    n = lis.current()


def audio_to_text():
    global showText,lis
    wn2 = tkinter.Tk()
    wn2.title("Speech to Text converter")
    wn2.geometry('500x500')
    wn2.config(bg='snow3')

    Label(wn2, text='Speech to Text converter',
          fg='black', font=('Courier', 15)).place(x=60, y=10)

    Label(wn2, text='Click the start and end buttons to speak and end speech').place(x=20, y=50)

    options = [
        "English",
        "Telugu",
        "Hindi",
        "Marathi",
        "Urdu",
        "Tamil",
        "Malayalam",
        "Kannada",
        "Bengali",
        "Punjabi"
    ]
    clicked =tkinter.StringVar()
    lis = ttk.Combobox(wn2,values = options, width = 10)
    lis.place(x= 100, y = 100)
    Button(wn2, text='Select', bg='ivory3', font=('Courier', 13),
           command=lambda:togetind()).place(x=200, y=100)
    Button(wn2, text='Start', bg='ivory3', font=('Courier', 13),
           command=takeCommand).place(x=300, y=100)


    Button(wn2, text='Stop', bg='ivory3', font=('Courier', 13),
           command=stop).place(x=400, y=100)

    v = Scrollbar(wn2, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    showText = Text(wn2, font=("Calibre, 14"), yscrollcommand=v.set)
    showText.focus()
    showText.place(x=20, y=130, width=450, height=300)

    v.config(command=showText.yview)
    wn2.mainloop()


voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)


def speak():
    global textBox
    text = textBox.get(1.0, "end-1c")
    print(text)
    voiceEngine.say(text)
    voiceEngine.runAndWait()


wn = tkinter.Tk()
wn.title(" Speech to Text converter")
wn.geometry('700x300')
wn.config(bg='LightBlue1')

Label(wn, text='Speech to Text converter',
      fg='black', font=('Courier', 15)).place(x=40, y=10)

global textBox, showText, command, go
go = 1

Button(wn, text="Convert Speech to Text", bg='ivory3', font=('Courier', 15),
       command=audio_to_text).place(x=230, y=150)

wn.mainloop()