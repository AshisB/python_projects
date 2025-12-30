from tkinter import *
import pyautogui
import ctypes
# Load the user32.dll library
user32 = ctypes.windll.user32


def auto_rotate():
    start_btn.config(state='disabled')
    next_app()

def next_app():
    # Method that should work on Windows 11
    print("rotating...")


    pyautogui.hotkey('alt', 'esc')


    # Maximize current window
    hwnd = user32.GetForegroundWindow()
    user32.ShowWindow(hwnd, 3)  # Maximize
    start_btn.after(5000, func=next_app)


# ui setup
screen=Tk()
screen.title('Auto Rotate')
screen.config(pady=10,padx=10,bg='#ffffff')

start_btn=Button(text='▶start',fg='green',command=auto_rotate)
start_btn.grid(row=0,column=0,padx=5)
pause_btn=Button(text='⏸️pause',fg='blue',command=auto_rotate)
pause_btn.grid(column=1,row=0,padx=5)
stop_btn=Button(text='🛑stop',fg='red',command=auto_rotate)
stop_btn.grid(column=2,row=0,padx=5)



screen.mainloop()