BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
from data_filter import DataFilter
from ui_setup import UI_SETUP



if __name__ == "__main__":

#--------------------------UI SETUP-----------------------------------------#
    window=Tk()
    window.title('Flash Card')
    window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

    user_choice=messagebox.askyesno('Start Game?','Do you want to play?')
    if user_choice:
        all_csv_data=DataFilter.GetData()
        ui=UI_SETUP(window,BACKGROUND_COLOR,all_csv_data)
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.mainloop()
    else:
        messagebox.showinfo('Thank You :)','Thank You! for playing.')
        
        






