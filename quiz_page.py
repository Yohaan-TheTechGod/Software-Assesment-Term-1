from tkinter import *
import customtkinter
from PIL import Image
import Main_File
import Quiz_easy
import Quiz_hard

def quiz_page():
    root = customtkinter.CTk()
    root.title('Alkali Metals Quiz')
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    bg = PhotoImage(file='Quiz_Background.png')
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def QUIZ_EASY():
        root.destroy()
        Quiz_easy.start_quiz()

    def QUIZ_HARD():
        root.destroy()
        Quiz_hard.start_quiz()

    def show_info_popup():
        popup = customtkinter.CTkToplevel(root)
        popup.geometry("500x350")
        popup.title("Information")
        popup.attributes("-topmost", True)
        popup_label = customtkinter.CTkLabel(popup, text="Easy or hard quiz options await.", font=("Helvetica", 48), justify="center")
        popup_label.pack(expand=True, pady=20)

    info_icon = customtkinter.CTkImage(light_image=Image.open("help_icon.png"), size=(40, 40))
    info_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    info_frame.pack(side="bottom", anchor="se", padx=10, pady=10)
    info_button = customtkinter.CTkButton(info_frame, image=info_icon, text="", width=48, height=48, command=show_info_popup, fg_color="transparent", hover_color="#333333", bg_color='black')
    info_button.pack()

    main_frame = customtkinter.CTkFrame(root, fg_color="black")
    main_frame.place(relx=0.5, rely=0.63, anchor="center")

    button_config = {
        "height": 80,
        "width": 230,
        "font": ("Helvetica", 24),
        "text_color": 'white',
        "corner_radius": 20,
        "fg_color": "#818181",
        "hover_color": "black",
        "bg_color": "black",  
        "border_width": 5,
        "border_color": 'white'
    }

    customtkinter.CTkButton(main_frame, text="Click for the Easy Quiz", command=QUIZ_EASY, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Click for the Hard Quiz", command=QUIZ_HARD, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Back to Main Menu", command=lambda: [root.destroy(), Main_File.main_page()], **button_config).pack(pady=10)

    root.mainloop()
