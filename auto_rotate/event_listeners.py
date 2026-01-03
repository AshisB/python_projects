from pynput import mouse,keyboard
from pynput.keyboard import Key
# import threading


class UserListener:
    def __init__(self):
        self.user_activity=False
        self.ui=None
        self.ignore_next_keys = False


    def event_listener(self):
        keyboard.Listener(on_press=self.on_key_press).start()
        mouse.Listener(on_click=self.on_mouse_click,on_scroll=self.on_mouse_click).start()


    def on_mouse_click(self, *args, **kwargs):
        self.user_activity=True
        print('detecting....')

    def on_key_press(self,keyboard_key):
        if self.ignore_next_keys:
            print(f"Ignoring simulated key: {keyboard_key}")
            self.ignore_next_keys = False
            return

        print(f"Real user key: {keyboard_key}")
        self.user_activity = True
        # 2. Check for F1/F2 hotkeys
        print(keyboard_key)
        try:
            if keyboard_key == Key.f12:
                print("F1 pressed - Manual forward rotation")
                if self.ui:
                    self.ui.cancel_rotation_timer()
                    self.ui.rotate_forward()  # This will call check_activity()
            elif keyboard_key == Key.f11:
                print("F2 pressed - Manual backward rotation")
                if self.ui:
                    self.ui.cancel_rotation_timer()  # Stop auto-timer
                    self.ui.rotate_backward()  # You need to add this method

        except:
            pass

    def reset_activity(self):
        self.user_activity=False

