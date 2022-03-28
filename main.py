from tkinter import *
window = Tk()
window.title('PrepareApp')
window.geometry('250x150')

greeting = Label(text = 'Kurwa jeż, jeż w centrum miasta')
greeting.pack()
button = Button(text = 'Gorące jeże w okolicy')
button.pack()

var = IntVar()
study = Radiobutton(text = 'Nauka', variable = var, value = 1)
study.pack()
play = Radiobutton(text = 'Grańsko', variable = var, value = 2)
play.pack()

submit = Button(text = 'Przygotuj')
submit.pack()

window.mainloop()