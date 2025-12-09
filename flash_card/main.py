BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *


#--------------------------UI SETUP-----------------------------------------#
window=Tk()
window.title('Flash Card')
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

try:
    canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
    card_front = PhotoImage(file='./images/card_front.png')
    canvas.create_image(410, 280, image=card_front)
    canvas.grid(row=0,column=0,columnspan=2)
except FileNotFoundError:
    Label(text='Card front File is Missing')


try:
    canvas=Canvas(width=100,height=100,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
    card_right=PhotoImage(file='./images/right.png')
    canvas.create_image(50,50,image=card_right)
    canvas.grid(row=1,column=0)
except FileNotFoundError:
    Label(text='Card Right File is Missing')

try:
    canvas_wrong=Canvas(width=100,height=100,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
    card_wrong=PhotoImage(file='./images/wrong.png')
    canvas_wrong.create_image(50,50,image=card_wrong)
    canvas_wrong.grid(row=1,column=1)
except FileNotFoundError:
    Label(text='Card Wrong File is Missing')






window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.mainloop()
