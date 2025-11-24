from tkinter import *

window=Tk()
window.title('Test')
window.minsize(width=500,height=500)


label=Label(text='Title head',font=('Arial',20,'bold'))
label.pack()

input=Entry(width=14)
input.pack()

def button_clicked():
    label['text']=input.get()

button=Button(text='Click Me',command=button_clicked)
button.pack()













window.mainloop()