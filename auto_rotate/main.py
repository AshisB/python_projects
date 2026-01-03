from tkinter import *
import pyautogui
import ctypes
from pynput import mouse,keyboard
from event_listeners import UserListener

class UI:
    def __init__(self,user_listen):
        self.user32 = ctypes.windll.user32
        self.user_listener=user_listen
        self.rotation_timer=None
        self.CreateUi()
        self.is_paused_flag=False

    def auto_rotate(self):
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.pause_btn.config(state='normal')

        print(self.user_listener.user_activity)

        # Method that should work on Windows 11
        print("rotating...")
        pyautogui.hotkey('alt', 'esc')
        # Maximize current window
        hwnd = self.user32.GetForegroundWindow()
        self.user32.ShowWindow(hwnd, 3)

        self.check_activity()

    def check_activity(self):
        self.cancel_rotation_timer()
        if not self.user_listener.user_activity:
            self.rotation_timer=self.start_btn.after(3000, func=self.auto_rotate)
            print(self.user_listener.user_activity)
        else:
            print(self.user_listener.user_activity)
            self.user_listener.reset_activity()
            self.start_btn.config(state='disabled')
            self.rotation_timer=self.start_btn.after(8000, self.check_activity)

    def cancel_rotation_timer(self):
        if self.rotation_timer:
            self.start_btn.after_cancel(self.rotation_timer)
            self.rotation_timer = None

    def pause(self):
        if not self.is_paused_flag:
            self.cancel_rotation_timer()
            self.stop_btn.config(state='disabled')
            self.start_btn.config(state='disabled')
            self.pause_btn.config(state='normal',fg='Orange')
            self.user_listener.reset_activity()
            self.is_paused_flag=True
        else:
            self.stop_btn.config(state='normal')
            self.start_btn.config(state='disabled')
            self.pause_btn.config(state='normal',fg='blue')
            self.is_paused_flag = False
            self.rotation_timer = self.start_btn.after(5000, self.check_activity)

    def stop(self):
        self.cancel_rotation_timer()
        self.stop_btn.config(state='disabled')
        self.start_btn.config(state='normal')
        self.pause_btn.config(state='disabled')
        self.user_listener.reset_activity()

    def rotate_forward(self):
        """Your existing forward rotation"""
        pyautogui.hotkey('alt', 'esc')
        hwnd = self.user32.GetForegroundWindow()
        self.user32.ShowWindow(hwnd, 3)
        self.user_listener.reset_activity()
        self.rotation_timer = self.start_btn.after(5000, self.check_activity)


    def rotate_backward(self):
        """Add backward rotation"""
        pyautogui.hotkey('alt', 'shift', 'esc')
        hwnd = self.user32.GetForegroundWindow()
        self.user32.ShowWindow(hwnd, 3)
        self.user_listener.reset_activity()
        self.rotation_timer = self.start_btn.after(5000, self.check_activity)




    # ui setup
    def CreateUi(self):
        self.start_btn=Button(text='▶start',fg='green',command=self.auto_rotate)
        self.start_btn.grid(row=0,column=0,padx=5)
        self.pause_btn=Button(text='⏸️pause',fg='blue',command=self.pause)
        self.pause_btn.grid(column=1,row=0,padx=5)
        self.stop_btn=Button(text='🛑stop',fg='red',command=self.stop)
        self.stop_btn.grid(column=2,row=0,padx=5)

if __name__=="__main__":
    screen = Tk()
    screen.title('Auto Rotate')
    screen.config(pady=10, padx=10, bg='#ffffff')
    user_listen = UserListener()
    ui=UI(user_listen)
    user_listen.ui=ui
    user_listen.event_listener()
    screen.mainloop()