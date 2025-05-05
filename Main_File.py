from tkinter import *
import customtkinter  # Custom version of tkinter for buttons
from PIL import Image  # For image processing
import quiz_page       # Allow code to open to this file
import about_page      # Allow code to open to this file
import learn_page      # Allow code to open to this file

def main_page():
    # Create the main application window
    root = customtkinter.CTk()
    root.title('Alkali Metals Quiz')
    
    # Set fullscreen mode and allow exiting fullscreen with Escape
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    # Set background image
    bg = PhotoImage(file='Main_background.png')
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define functions to navigate to other pages
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

    # Display a pop-up with instructions when help icon is clicked
    def show_info_popup():
        popup = customtkinter.CTkToplevel(root)
        popup.geometry("900x600")
        popup.title("Information")
        popup.attributes("-topmost", True)

        # Set background for the popup
        bg_image = customtkinter.CTkImage(light_image=Image.open("Help_Background.png"), size=(1920, 1080))
        bg_label = customtkinter.CTkLabel(popup, image=bg_image, text="")
        bg_label.image = bg_image  # Prevent garbage collection by python Tkinter
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Help text
        popup_label = customtkinter.CTkLabel(
            popup,
            text=(
                "This app lets you learn and test your knowledge about alkali metals.\n"
                "Click the buttons to begin\n"
                "The Learn Button will lead you to the learn page, where you can learn all about Alkali Metals.\n"
                "The Quiz button will test your knowledge, and the about button, well you got to find out for yourself :)\n"
                "The Exit button will close the program"
            ),
            font=("Helvetica", 32), justify="center", text_color="black", fg_color='#82ADFE', wraplength=800)
        popup_label.place(relx=0.5, rely=0.5, anchor="center")

        # Close button in popup
        close_button = customtkinter.CTkButton(
            popup, text="Close Window ❌", font=("Helvetica", 32), command=popup.destroy)
        close_button.place(relx=0.5, rely=0.85, anchor="center")

    # Help icon in corner
    info_icon = customtkinter.CTkImage(light_image=Image.open("help_icon.png"), size=(40, 40))
    info_frame = customtkinter.CTkFrame(root, fg_color="orange", bg_color='orange')
    info_frame.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    # Button that opens the popup
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

    # Frame to hold the main buttons
    main_frame = customtkinter.CTkFrame(root, fg_color="#BDEAF6", bg_color="#BDEAF6")
    main_frame.place(relx=0.5, rely=0.615, anchor="center")

    # Common style for all buttons
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

    # Add buttons to the main menu
    customtkinter.CTkButton(main_frame, text="Click to Learn", command=LEARN, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Click for the Quiz", command=QUIZ, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="About this Project", command=ABOUT, **button_config).pack(pady=10)
    customtkinter.CTkButton(main_frame, text="Exit", command=EXIT, **button_config).pack(pady=10)

    # Start the GUI loop
    root.mainloop()

# Run the main page if this file is executed directly
if __name__ == "__main__":
    main_page()