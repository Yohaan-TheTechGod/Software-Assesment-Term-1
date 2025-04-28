from tkinter import *
import customtkinter
from PIL import Image
import quiz_page
import about_page
import learn_page

def main_page():
    root = customtkinter.CTk()
    root.title('Alkali Metals Quiz')
    root.attributes('-fullscreen', True)  
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    bg = PhotoImage(file='Main_background.png')
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def LEARN():
        root.destroy()
        learn_page.learn_page()

    def QUIZ():
        root.destroy()
        quiz_page.quiz_page()

    def ABOUT():
        root.destroy()
        about_page.about_page()

    def EXIT():
        root.destroy()

    def show_info_popup():
        popup = customtkinter.CTkToplevel(root)
        popup.geometry("500x350")
        popup.title("Information")
        popup.attributes("-topmost", True)
        popup_label = customtkinter.CTkLabel(popup, text="This app lets you learn and test your knowledge about alkali metals.\nClick the buttons to begin\nThe Learn Button will lead you to the learn page, where you can learn all about Alkali Metals.\nThe Quiz button will test your knowledge, and the about button, well you got to find out for yourself :)\nThe Exit button will close the program", font=("Helvetica", 36), justify="center")

        popup_label.pack(expand=True, pady=20)

    info_icon = customtkinter.CTkImage(light_image=Image.open("help_icon.png"), size=(40, 40))
    info_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    info_frame.pack(side="bottom", anchor="se", padx=10, pady=10)
    info_button = customtkinter.CTkButton(info_frame, image=info_icon, text="", width=48, height=48, command=show_info_popup, fg_color="transparent", hover_color="#333333", bg_color='black')
    info_button.pack()

    main_frame = customtkinter.CTkFrame(root, fg_color="black")
    main_frame.place(relx=0.5, rely=0.6, anchor="center")  

    button_config = {
        "height": 80,
        "width": 230,
        "font": ("Helvetica", 24),
        "text_color": 'white',
        "corner_radius": 20,
        "fg_color": "#818181",
        "hover_color": "#black",
        "bg_color": "black",  
        "border_width": 5,
        "border_color": 'white'
    }

    customtkinter.CTkButton(main_frame, text="Click to Learn", command=LEARN, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Click for the Quiz", command=QUIZ, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="About this Project", command=ABOUT, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Exit", command=EXIT, **button_config).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_page()
