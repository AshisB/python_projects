import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
from encrypt_decrypt import Encryption



encryption=Encryption()

# colors
all_buttons={}
button_colors = [
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
    "#5A7D9A",   # 25. Slate Blue - Muted blue-gray
]


#------------------------------SEARCH CREDENTIALS--------------------------------#
def SetPassword(password,email,website):
     pyperclip.copy(password)
     for button in all_buttons:
         all_buttons[button].config(bg=choice(button_colors))
     all_buttons[website].config(bg='white',fg='black')
     # messagebox.showinfo('website', f'Your Email/Username:{email}\nYour Password:{password}')




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('MyPass')
# window.config(padx=50,pady=50)

# # Adding logo
# canvas=Canvas(height=200,width=200)
# logo_name=PhotoImage(file='./logo.png')
# canvas.create_image(100,100,image=logo_name)
# canvas.grid(row=0,column=1)

#Adding Labels

# website_label=Label(text='Websites:',font=('Arial',9,'bold'))
# website_label.grid(row=1,column=0)

#-----------------------------------Creating buttons for each sites--------------------------------#

try:
    with open('data.json','r') as f:
        all_data = json.load(f)
except FileNotFoundError:
    messagebox.showerror('Sorry!File not found :)')
else:
    all_data=encryption.decrypt(all_data)
    sorted_data=dict(sorted(all_data.items()))
    counter=0

    for data in sorted_data:
        email,password=next(iter(sorted_data[data].items()))
        search_button = Button(text=data, bg=choice(button_colors), fg='white' ,command=lambda user_password=password,user_email=email,website_data=data: SetPassword(user_password,user_email,website_data))
        search_button.grid(row=0, column=counter, sticky='ew', pady=5, padx=5)
        all_buttons[data]=search_button
        counter+=1
#Searching Credentials










window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
