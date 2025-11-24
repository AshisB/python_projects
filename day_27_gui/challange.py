from tkinter import *


def ClickButton():
    print('button first clicked')
    label['text']=input.get()

def ClickNewButton():
    print('new button clicked')
    label['text']='New Form'


window=Tk()
window.title('New Form')
window.minsize(width=500,height=500)


label=Label(text="New Form",font=('Arial',10,'bold'))
label.grid(row=0,column=0)

button=Button(text='Click Me',command=ClickButton)
button.grid(row=1,column=1)

button=Button(text='Click Me',command=ClickNewButton)
button.grid(row=0,column=2)

input=Entry(width=50)
input.insert(END,string='Please enter your name..')
input.grid(row=2,column=3)

window.mainloop()

