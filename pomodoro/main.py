from tkinter import *
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timer=None
# ---------------------------- TIMER RESET ------------------------------- #

def ResetButton():
    global reps,timer
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(canvas_text, text='00:00')
    checker_label.config(text="")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def StartButton():
    global reps
    if reps<=8:
        if reps==8:
            CountDown(LONG_BREAK_MIN*60)
            timer_label.config(text='Break',fg=RED)
        elif reps%2==0:
            CountDown(SHORT_BREAK_MIN *60)
            timer_label.config(text='Break',fg=PINK)
        elif reps%2!= 0:
            CountDown(WORK_MIN*60)
            timer_label.config(text='Work',fg=GREEN)

    else:
        timer_label.config(text='Done', fg='blue')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def CountDown(count):
    global reps,timer
    if count>=0:
        minute=count//60
        seconds=count%60
        if seconds<10:
            seconds=f'0{seconds}'

        canvas.itemconfig(canvas_text, text=f'{minute}:{seconds}')
        timer=window.after(1000, CountDown, count - 1)
    else:
        if reps%2==0:
            checker_label.config(text=f'{"✔"*int(reps/2)}')
            window.attributes('-topmost', False)
        else:
            window.lift()
            window.focus_force()
            window.attributes('-topmost', True)
            winsound.Beep(1000, 2000)

        reps += 1
        StartButton()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Pomodoro')
window.config(padx=40,pady=40,bg=YELLOW)



#Timer label initiation
timer_label=Label(text='Timer',bg=YELLOW,fg=GREEN,font=(FONT_NAME,60,'bold'))
timer_label.grid(row=0,column=1)

# Using canvas pomodoro image initiation
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightbackground=YELLOW)
tomato_img=PhotoImage(file='./tomato.png')
canvas.create_image(102,112,image=tomato_img)
canvas_text=canvas.create_text(102,130,text='00:00',fill='white',font=(FONT_NAME,25,'bold'))
canvas.grid(row=1,column=1)

#setting button start
start_button=Button(text='start',bg='green',activebackground=GREEN,command=StartButton)
start_button.grid(row=2,column=0)

#setting button reset
reset_button=Button(text='reset',bg='red',activebackground=PINK,command=ResetButton)
reset_button.grid(row=2,column=2)

#setting for the checker
checker_label=Label(text='',bg=YELLOW,fg='green',font=(FONT_NAME,12,'bold'))
checker_label.grid(row=3,column=1)


















window.mainloop()