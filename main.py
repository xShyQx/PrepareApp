import tkinter as tk
window = tk.Tk()
window.title('Kurwa Jeż')
window.geometry('500x400')

greeting = tk.Label(text = 'Kurwa jeż, jeż w centrum miasta')
greeting.pack()
button = tk.Button(text = 'Gorące jeże w okolicy')
button.pack()

window.mainloop()