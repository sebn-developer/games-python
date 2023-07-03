from gtts import gTTS
import os

mytext = input("Enter a text")
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("hai.mp3")
os.system("mpg321 hai.mp3")

# from typing import runtime_checkable
# import pyttsx3 
# import random
# from tkinter import *
# from tkinter import ttk
# import tkinter as tk
# window = tk.Tk()



# class texttospeech:
#     def __init__(self,window):
#         self.window = window
#         self.window.title("Text to Speech  ")
#         self.window.geometry("500x200+0+0")
        
#         title = Label(self.window,text="Text to Speech",bd=0,font=("times new roman",15,"bold"),bg="white",fg="magenta")
#         title.pack(side=TOP,fill=X)

#         mystring = tk.StringVar(window)

#         def clear():
#                 mystring.set("")
                


#         def Speech():

#                 mes = mystring.get()                    
#                 engine = pyttsx3.init('sapi5')          
#                 voices = engine.getProperty('voices')   
#                 engine.say('{}'.format(mes))            
#                 engine.runAndWait()

#         text1 = Entry(self.window,textvariable=mystring,width=100,fg="blue",bd=3,selectbackground='violet')
#         text1.place(x=0,y=20,height=50,width=500)

#         run_button = Button(self.window,text=" Speak ", command=Speech)
#         run_button.place(x=20,y=100,height=50,width=70)

#         clr_button = Button(self.window,text=" clear ", command=clear)
#         clr_button.place(x=250,y=100,height=50,width=70)



# ob = texttospeech(window)
# window.mainloop()
