from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess

dane = open('dane.txt', 'r')
window = Tk()
window.title('PrepareApp')
window.geometry('250x150')

greeting = Label(text = 'Kurwa jeż, jeż w centrum miasta').pack()
button = Button(text = 'Gorące jeże w okolicy').pack()

var_choice = IntVar(window, 0)
study = Radiobutton(text = 'Nauka', variable = var_choice, value = 1).pack()
play = Radiobutton(text = 'Grańsko', variable = var_choice, value = 2).pack()

def prepare():
    choice = var_choice.get()
    if(choice == 0):
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    elif(choice == 1):
        web = False
        app = False
        for line in dane:
            line = line[:-1]
            if(line == '-- Strony internetowe --'):
                web = True
            elif(line == '-- Programy --'):
                web = False
                app = True
            elif(app == True):
                subprocess.Popen([line])
            elif(web == True):
                webbrowser.open(line)
    elif(choice == 2):
        print('j33ż')

submit = Button(text = 'Przygotuj', command = prepare).pack()
settings = Button(text = 'Ustawienia').pack()

window.mainloop()