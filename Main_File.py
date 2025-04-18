from tkinter import *
import customtkinter
from PIL import Image

#root = Tk()
root = customtkinter.CTk()
root.title('Alkali Metals Quiz')
root.geometry("800x600")

#defined the image for the background
bg = PhotoImage(file='background.png')
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#functions for the regular buttons
def LEARN():
    pass

def QUIZ():
    pass

def ABOUT():
    pass

def EXIT():
    root.destroy()

#help icon popup
def show_info_popup():
    popup = customtkinter.CTkToplevel(root)
    popup.geometry("500x350")
    popup.title("Information")
    popup.attributes("-topmost", True)
    popup_label = customtkinter.CTkLabel(popup, text="This app lets you learn and test your knowledge about alkali metals.\nClick the buttons to begin\nThe Learn Button will lead you to the learn page, where you can learn all about Alkali Metals.\nThe Quiz button will test your knowledge, and the about button, well you got to find out for yourself :)\nThe Exit button will close the program", font=("Helvetica", 16), justify="center")
    popup_label.pack(expand=True, pady=20)

# Responsive Help Icon Button frame with meta data
info_icon = customtkinter.CTkImage(light_image=Image.open("help_icon.png"), size=(40, 40))
info_frame = customtkinter.CTkFrame(root, fg_color="transparent")
info_frame.pack(side="bottom", anchor="se", padx=10, pady=10)
info_button = customtkinter.CTkButton(info_frame, image=info_icon, text="", width=48, height=48, command=show_info_popup,fg_color="transparent", hover_color="#333333", bg_color='black')
info_button.pack()

# title + buttons repsonsive frame
main_frame = customtkinter.CTkFrame(root, fg_color="black")
main_frame.place(relx=0.5, rely=0.63, anchor="center")  

title_label = customtkinter.CTkLabel(
    main_frame,
    text="Alkali Metals Quiz",
    font=("Helvetica", 65),
    text_color='white',
    fg_color='black',
    bg_color='black'
)
title_label.pack(pady=(0, 30))

button_config = {
    "height": 80,
    "width": 230,
    "font": ("Helvetica", 24),
    "text_color": 'white',
    "corner_radius": 20,
    "fg_color": "#818181",
    "hover_color": "#3B3B3B",
    "bg_color": "black",  
    "border_width": 5,
    "border_color": 'white'
}

learn_button = customtkinter.CTkButton(main_frame, text="Click to Learn", command=LEARN, **button_config)
learn_button.pack(pady=10)

quiz_button = customtkinter.CTkButton(main_frame, text="Click for the Quiz", command=QUIZ, **button_config)
quiz_button.pack(pady=10)

about_button = customtkinter.CTkButton(main_frame, text="About this Project", command=ABOUT, **button_config)
about_button.pack(pady=10)

exit_button = customtkinter.CTkButton(main_frame, text="Exit", command=EXIT, **button_config)
exit_button.pack(pady=10)

root.mainloop()