from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def GeneratePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[]

    password_letters = [choice(letters) for _ in range(randint(9, 11))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =[choice(numbers) for _ in range(randint(3, 5))]
    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)

    result_password = "".join(password_list)
    password.insert(0, result_password)

    pyperclip.copy(result_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def SavePassword():
    website_data=website.get()
    email_data=email.get()
    password_data=password.get()


    # validating form fields whether they are empty or not
    if len(website_data)<=0:
        website.config(highlightbackground='red', highlightthickness=2)
        website_label.config(fg='red')
        messagebox.showerror(title='Error',message='!!Missing Website')
    elif len(email_data)<=0:
        email.config(highlightbackground='red', highlightthickness=2)
        email_label.config(fg='red')
        messagebox.showerror(title='Error', message='!!Missing Email')
    elif len(password_data)<=0:
        password.config(highlightbackground='red', highlightthickness=2)
        password_label.config(fg='red')
        messagebox.showerror(title='Error', message='!!Missing Password')
    else:
        isok=messagebox.askokcancel(title=website_data,message=f"These are the details entered:\nWebsite:{website_data}\nEmail:{email_data}\nPassword:{password_data}")
        if isok:
            userdata=f'{website_data},{email_data},{password_data}\n'
            with open('data.txt','a') as f:
                f.write(userdata)
                email.delete(0,END)
                password.delete(0,END)
                website.delete(0,END)
                messagebox.showinfo(title='Message',message='Successfully Added!!')



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('MyPass')
window.config(padx=50,pady=50)

# Adding logo
canvas=Canvas(height=200,width=200)
logo_name=PhotoImage(file='./logo.png')
canvas.create_image(100,100,image=logo_name)
canvas.grid(row=0,column=1)

#Adding Labels

website_label=Label(text='Website:')
website_label.grid(row=1,column=0)


email_label=Label(text='Email/Username:')
email_label.grid(row=2,column=0)

password_label=Label(text='Password:')
password_label.grid(row=3,column=0)


#Adding Entries

website=Entry(width=35)
website.grid(row=1, column=1, columnspan=2, sticky='ew',pady=5,padx=5)
website.focus()

email=Entry(width=35)
email.grid(row=2, column=1, columnspan=2, sticky='ew',pady=5,padx=5)


password=Entry(width=21)
password.grid(row=3, column=1, sticky='ew',pady=5,padx=5)

#Adding password

password_generate_button=Button(text='Generate Password',bg='blue',fg='white',command=GeneratePassword)
password_generate_button.grid(row=3, column=2, sticky='ew',pady=5,padx=5)

#Adding Add Button

add_button=Button(text='+Add',bg='green',fg='white',command=SavePassword)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew',pady=5,padx=5)









window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
