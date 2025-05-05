from tkinter import *
import customtkinter
from PIL import Image
import Main_File           # To return to main menu
import Quiz_easy           # Allow code to open to this file
import Quiz_hard           # Allow code to open to this file

def quiz_page():
    # Initialize the main quiz window
    root = customtkinter.CTk()
    root.title('Alkali Metals Quiz')
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    # Set background image
    bg = PhotoImage(file='Quiz_Page_Background.png')
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Start the easy quiz
    def QUIZ_EASY():
        root.destroy()
        Quiz_easy.start_quiz()

    # Start the hard quiz
    def QUIZ_HARD():
        root.destroy()
        Quiz_hard.start_quiz()

    # Display info popup with instructions
    def show_info_popup():
        popup = customtkinter.CTkToplevel(root)
        popup.geometry("900x600")
        popup.title("Information")
        popup.attributes("-topmost", True)

        # Background for popup
        bg_image = customtkinter.CTkImage(light_image=Image.open("Help_Background.png"), size=(1920, 1080))
        bg_label = customtkinter.CTkLabel(popup, image=bg_image, text="")
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Instructional text
        popup_label = customtkinter.CTkLabel(
            popup,
            text=("Easy or hard quiz options await\nWanna go back to learn page?\nClick the Back to Main Menu Button and click Learn"),
            font=("Helvetica", 48), justify="center", text_color="black", fg_color='#82ADFE', wraplength=800)
        popup_label.place(relx=0.5, rely=0.5, anchor="center")

        # Close popup button
        close_button = customtkinter.CTkButton(
            popup, text="Close Window ❌", font=("Helvetica", 32), command=popup.destroy)
        close_button.place(relx=0.5, rely=0.85, anchor="center")

    # Help icon and button (bottom-right corner)
    info_icon = customtkinter.CTkImage(light_image=Image.open("help_icon.png"), size=(40, 40))
    info_frame = customtkinter.CTkFrame(root, fg_color="orange", bg_color='orange')
    info_frame.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
    info_button = customtkinter.CTkButton(
        info_frame,
        image=info_icon,
        text="",
        width=48,
        height=48,
        command=show_info_popup,
        fg_color="orange",
        hover_color="black",
        bg_color='orange'
    )
    info_button.pack()

    # Frame for quiz buttons
    main_frame = customtkinter.CTkFrame(root, fg_color="#BDEAF6", bg_color="#BDEAF6")
    main_frame.place(relx=0.5, rely=0.6, anchor="center")

    # Styling for all buttons
    button_config = {
        "height": 80,
        "width": 230,
        "font": ("Helvetica", 24),
        "text_color": 'white',
        "corner_radius": 20,
        "fg_color": "#BDEAF6",
        "hover_color": "black",
        "bg_color": "#BDEAF6",
        "border_width": 5,
        "border_color": 'white'
    }

    # Quiz difficulty and navigation buttons
    customtkinter.CTkButton(main_frame, text="Click for the Easy Quiz", command=QUIZ_EASY, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Click for the Hard Quiz", command=QUIZ_HARD, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Back to Main Menu", command=lambda: [root.destroy(), Main_File.main_page()], **button_config).pack(pady=10)

    # Start the main event loop
    root.mainloop()