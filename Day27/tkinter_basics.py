import tkinter
from tkinter.ttk import *

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=600, height=500)
# window.pack()

label = tkinter.Label(text="I from label", font=("Roboto", 24, "bold"))
# label.pack()
# label.pack(side="left")
label.grid(row=0, column=0)
label["text"] = "new text"
label.config(text="new text")

def button_clicked():
    new_text =input.get()
    label.config(text=new_text)
    

button = Button(text="click me", command=button_clicked)
button.grid(row=1, column=1)

input = Entry()
input.grid(row=2, column=3)

window.mainloop() 