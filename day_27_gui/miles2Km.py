#this is the program to  convert miles to kilometer
from tkinter import *

#functions
def Calculate():
    miles=float(input.get())
    kilometers=miles*1.60934
    output.config(text=str(kilometers))

window=Tk()
window.title('Mile to Km Converter')
window.minsize(width=300,height=150)
window.config(padx=30,pady=30)


label1=Label(text='is equal to',font=('Arial',10,'bold'))
label1.grid(row=1,column=0)
label1.config(padx=5,pady=5)

#input here
input=Entry(width=20)
input.grid(row=0,column=1)

label2=Label(text='Miles',font=('Arial',10,'bold'))
label2.grid(row=0,column=2)
label2.config(padx=5,pady=5)

#outputt here
output=Label(text='0',font=('Arial',10,'bold'))
output.grid(row=1,column=1)

label4=Label(text='Km',font=('Arial',10,'bold'))
label4.grid(row=1,column=2)

button=Button(text='Calculate',command=Calculate)
button.grid(row=2,column=1)




window.mainloop()