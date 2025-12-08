import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import os
import sys
from encrypt_decrypt import Encryption
from tkinter import simpledialog





class MyApp:
    def __init__(self,window,entered_password):
        self.canvas = None
        self.encryption=Encryption()
        self.window=window
        self.CreateWidgets()
        self.entered_password=entered_password


    def resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)



    # ------------------------------SEARCH CREDENTIALS--------------------------------#
    def SearchCredentials(self):

        website_name = self.website.get().lower()
        try:
            with open('data.json') as f:
                all_data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror('OOPS', 'No data in file')
        else:
            all_data = self.encryption.decrypt(all_data,self.entered_password)
            search_data = {key.lower(): value for key, value in all_data.items()}
            if website_name in search_data:
                email, password = next(iter(search_data[website_name].items()))
                pyperclip.copy(password)
                messagebox.showinfo(website_name, f'Your Email/Username:{email}\nYour Password:{password}')
                # Adding Add Button
                self.add_button.grid_remove()
                self.delete_button = Button(text='-Delete', bg='red', fg='white', command=lambda website=website_name:self.DeletePassword(website))
                self.delete_button.grid(row=4, column=1, columnspan=2, sticky='ew', pady=5, padx=5)

            else:
                messagebox.showerror('Oops', f'Sorry!No data available for {website_name}')


    #delete password
    def DeletePassword(self,website_name):
        with open('data.json', 'r') as f:
            all_data = json.load(f)
            all_data = self.encryption.decrypt(all_data, self.entered_password)
            if website_name in all_data:
                del all_data[website_name]
            all_data.update(all_data)
            encrypted_data = self.encryption.encrypt(all_data, self.entered_password)
            with open('data.json', 'w') as f:
                json.dump(encrypted_data, f, indent=4)

            self.website.delete(0, END)
            self.delete_button.destroy()
            self.add_button.grid(row=4, column=1, columnspan=2, sticky='ew', pady=5, padx=5)

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    # Password Generator Project
    def GeneratePassword(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = []

        password_letters = [choice(letters) for _ in range(randint(9, 11))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(3, 5))]
        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        result_password = "".join(password_list)
        self.password.insert(0, result_password)

        pyperclip.copy(result_password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def SavePassword(self):
        website_data = self.website.get().lower()
        email_data = self.email.get()
        password_data = self.password.get()

        # validating form fields whether they are empty or not
        if len(website_data) <= 0:
            self.website.config(highlightbackground='red', highlightthickness=2)
            self.website_label.config(fg='red')
            messagebox.showerror(title='Error', message='!!Missing Website')
        elif len(email_data) <= 0:
            self.email.config(highlightbackground='red', highlightthickness=2)
            self.email_label.config(fg='red')
            messagebox.showerror(title='Error', message='!!Missing Email')
        elif len(password_data) <= 0:
            self.password.config(highlightbackground='red', highlightthickness=2)
            self.password_label.config(fg='red')
            messagebox.showerror(title='Error', message='!!Missing Password')
        else:
            isok = messagebox.askokcancel(title=website_data,
                                          message=f"These are the details entered:\nWebsite:{website_data}\nEmail:{email_data}\nPassword:{password_data}")
            if isok:
                userdata = {
                    website_data: {
                        email_data: password_data
                    }
                }

                try:
                    with open('data.json', 'r') as f:
                        all_data = json.load(f)
                except FileNotFoundError:
                    userdata = self.encryption.encrypt(userdata,self.entered_password)
                    with open('data.json', 'w') as f:
                        json.dump(userdata, f, indent=4)
                else:
                    all_data = self.encryption.decrypt(all_data,self.entered_password)
                    all_data.update(userdata)
                    encrypted_data =  self.encryption.encrypt(all_data,self.entered_password)
                    with open('data.json', 'w') as f:
                        json.dump(encrypted_data, f, indent=4)
                finally:
                    self.email.delete(0, END)
                    self.password.delete(0, END)
                    self.website.delete(0, END)
                    messagebox.showinfo(title='Message', message='Successfully Added!!')

    def CreateWidgets(self):
        self.window.config(padx=50, pady=50)
        # Adding logo
        try:
            self.canvas = Canvas(height=200, width=200)
            self.logo_name = PhotoImage(file=self.resource_path('./logo.png'))
            self.canvas.create_image(100, 100, image=self.logo_name)
            self.canvas.grid(row=0, column=1)
        except Exception:
            Label(text="🔒 My Pass", font=("Arial", 24, "bold")).grid(column=1, row=0)
        # Adding Labels

        self.website_label = Label(text='Website:')
        self.website_label.grid(row=1, column=0)

        self.email_label = Label(text='Email/Username:')
        self.email_label.grid(row=2, column=0)

        self.password_label = Label(text='Password:')
        self.password_label.grid(row=3, column=0)

        # Adding Entries

        self.website = Entry(width=35)
        self.website.grid(row=1, column=1, sticky='ew', pady=5, padx=5)
        self.website.focus()

        self.email = Entry(width=35)
        self.email.insert(0, 'ashis.maharjan@sanimabank.com')
        self.email.grid(row=2, column=1, columnspan=2, sticky='ew', pady=5, padx=5)

        self.password = Entry(width=21)
        self.password.grid(row=3, column=1, sticky='ew', pady=5, padx=5)

        # Searching Credentials

        self.search_button = Button(text='Search', bg='blue', fg='white', command=self.SearchCredentials)
        self.search_button.grid(row=1, column=2, sticky='ew', pady=5, padx=5)

        # Adding password

        self.password_generate_button = Button(text='Generate Password', bg='blue', fg='white', command=self.GeneratePassword)
        self.password_generate_button.grid(row=3, column=2, sticky='ew', pady=5, padx=5)

        # Adding Add Button

        self.add_button = Button(text='+Add', bg='green', fg='white', command=self.SavePassword)
        self.add_button.grid(row=4, column=1, columnspan=2, sticky='ew', pady=5, padx=5)


#
#
class MasterPass():
    def __init__(self,window):
        self.window=window
        self.CreatePasswordWidgets()
        self.encryption = Encryption()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def VerifyPassword(self):
        entered_password=self.master_password.get()
        if not os.path.exists('master.hash'):
            response = messagebox.askyesno(
                "First Time Setup",
                "Create new vault with this password?\n\n"
                "IMPORTANT: Never forget this password!\n"
                "Data cannot be recovered if lost."
            )
            if response:

                self.encryption.create_master_hash(entered_password)
                self.encryption.master_password= entered_password
                self.encryption.save_to_file({}, "passwords.enc")  # Test it works
                self.ShowMyApp(entered_password)
        else:
            if not self.encryption.verify_master_hash(entered_password):
                messagebox.showerror("Error", "Wrong password hash!")
                return

            if not os.path.exists('passwords.enc'):
                # Hash correct but vault missing = corrupted!
                messagebox.showerror("Error", "Vault file missing!")
                return
            else:
                try:
                    self.encryption.master_password = entered_password
                    data = self.encryption.load_from_file("passwords.enc")  # Try to open
                    self.ShowMyApp(entered_password)  # Pass to main app
                except:
                    messagebox.showerror("Error", "Wrong password!")





    def ShowMyApp(self,entered_password):
        for widget in self.window.winfo_children():
            widget.destroy()

        #now we are redirecting to another window based on users choice.
        from save_password import MyApp
        dialog = simpledialog.askstring("Choose", "Where to go?\nType 'A' to Add Passwords or 'V' to View Passwords: ").lower()
        if dialog == "a":
            self.app = MyApp(self.window, entered_password)
        elif dialog=='v':
            self.app = ViewPass(self.window, entered_password)
        else:
            self.ShowMyApp(entered_password)



    def CreatePasswordWidgets(self):
        self.window.config(padx=50, pady=50)
        # Clear any existing widgets first
        for widget in self.window.winfo_children():
            widget.destroy()
        # Adding logo
        try:
            self.canvas = Canvas(height=200, width=200)
            self.logo_name = PhotoImage(file=self.resource_path('./logo.png'))
            self.canvas.create_image(100, 100, image=self.logo_name)
            self.canvas.grid(row=0, column=1)
        except Exception:
            Label(text="🔒 My Pass", font=("Arial", 24, "bold")).grid(column=1, row=0)

        # Adding Labels

        self.master_password_label = Label(text='Master Password:')
        self.master_password_label.grid(row=1, column=0)


        # Adding Entries

        self.master_password = Entry(width=35)
        self.master_password.grid(row=1, column=1, columnspan=2, sticky='ew', pady=5, padx=5)
        self.master_password.focus()
        self.master_password.bind('<Return>',lambda e: self.VerifyPassword() if self.master_password.get().strip() else None)

        # Adding Unlock/Save Button

        self.add_button = Button(text='Unlock', bg='green', fg='white', command=self.VerifyPassword)
        self.add_button.grid(row=2, column=1, columnspan=2, sticky='ew', pady=5, padx=5)

class ViewPass:

    def __init__(self,window,master_password):
        # colors
        self.all_buttons = {}
        self.button_colors = [
            "#2E5894",  # 1. Blue Sapphire - Deep, trustworthy blue
            "#1560BD",  # 2. Denim Blue - Modern, calm blue
            "#1E6FD9",  # 3. Royal Blue - Vibrant but not harsh
            "#3A7CA5",  # 4. Steel Blue - Muted professional blue
            "#2E8B57",  # 5. Sea Green - Natural, success green
            "#3A9D5B",  # 6. Emerald - Fresh, positive green
            "#4C956C",  # 7. Forest Green - Earthy, stable green
            "#008080",  # 8. Teal - Balanced, creative
            "#48A9A6",  # 9. Verditer - Soft teal-blue
            "#5F9EA0",  # 10. Cadet Blue - Gentle, calming
            "#6A5ACD",  # 11. Slate Blue - Creative purple-blue
            "#7B68EE",  # 12. Medium Slate Blue - Friendly purple
            "#9370DB",  # 13. Medium Purple - Calm, premium feel
            "#B68D40",  # 14. Husk - Warm golden brown
            "#C19A6B",  # 15. Camel - Soft earthy tone
            "#708090",  # 16. Slate Gray - Professional neutral
            "#778899",  # 17. Light Slate Gray - Light neutral
            "#5C8D6F",  # 18. Sage Green - Muted natural green
            "#6AAAA0",  # 19. Polished Pine - Soft green-teal
            "#9461C2",  # 20. Amethyst - Gentle purple
            "#8B7355",  # 21. Burlywood Dark - Warm neutral
            "#367588",  # 22. Teal Blue - Deep calming teal
            "#228B22",  # 23. Forest Green (vibrant) - Success color
            "#CD5C5C",  # 24. Indian Red - Soft warning red (use sparingly)
            "#5A7D9A",  # 25. Slate Blue - Muted blue-gray
        ]
        self.window = window
        self.master_password = master_password
        self.encryption = Encryption()
        self.CreatePasswordTabs()



    # -----------------------------------Creating buttons for each sites--------------------------------#
    def CreatePasswordTabs(self):
        self.window.config(padx=1, pady=1)
        try:
            with open('data.json') as f:
                view_all_data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror('OOPS', 'No data in file')
        else:
            all_data = self.encryption.decrypt(view_all_data, self.master_password)

            sorted_data = dict(sorted(all_data.items()))
            counter_x = 0
            counter_y=0

            for data in sorted_data:
                email, password = next(iter(sorted_data[data].items()))
                search_button = Button(text=data, bg=choice(self.button_colors), fg='white',
                                       command=lambda user_password=password, user_email=email,
                                                      website_data=data: self.SetPassword(user_password, user_email,
                                                                                     website_data))
                search_button.grid(row=counter_x, column=counter_y, sticky='ew', pady=5, padx=5)
                if counter_y < 1:
                    counter_y += 1
                else:
                    counter_x += 1
                    counter_y = 0
                self.all_buttons[data] = search_button


    def SetPassword(self,password, email, website):
        pyperclip.copy(password)
        for button in self.all_buttons:
            self.all_buttons[button].config(bg=choice(self.button_colors))
        self.all_buttons[website].config(bg='white', fg='black')


# ---------------------------- UI SETUP ------------------------------- #

# Simple launcher
if __name__ == "__main__":

    def resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    window=Tk()
    window.title('MyPass')


    masterpass = MasterPass(window)
    # app = MyApp(window)




    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)

    window.mainloop()











