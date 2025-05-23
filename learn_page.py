from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import Main_File  # To return to the main menu

def learn_page():
    # Fullscreen window
    root = customtkinter.CTk()
    root.title("Learning Page")
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    # Set background image
    bg = PhotoImage(file='Learn_Background.png')
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Function to open a popup with info on each element
    def open_info_window(image_file, title):
        popup = customtkinter.CTkToplevel(root)
        popup.geometry("900x600")
        popup.title(title)
        popup.attributes("-topmost", True)

        bg_image = customtkinter.CTkImage(light_image=Image.open(image_file), size=(1920, 1080))
        bg_label = customtkinter.CTkLabel(popup, image=bg_image, text="")
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Close button
        close_button = customtkinter.CTkButton(
            popup, text="Close Window ❌", font=("Helvetica", 32), command=popup.destroy)
        close_button.place(relx=0.5, rely=0.875, anchor="center")

    # Dictionary mapping element names to their image and popup command
    element_buttons = {
        "Lithium": ("Lithium.png", lambda: open_info_window("Lithium_Info.png", "Lithium")),
        "Sodium": ("Sodium.png", lambda: open_info_window("Sodium_Info.png", "Sodium")),
        "Potassium": ("Potassium.png", lambda: open_info_window("Potassium_Info.png", "Potassium")),
        "Rubidium": ("Rubidium.png", lambda: open_info_window("Rubidium_Info.png", "Rubidium")),
        "Caesium": ("Caesium.png", lambda: open_info_window("Caesium_Info.png", "Caesium")),
        "Francium": ("Francium.png", lambda: open_info_window("Francium_Info.png", "Francium")),
    }

    # Frame to organize element buttons in a grid
    grid_frame = customtkinter.CTkFrame(root, fg_color="#BDEAF6", bg_color="#BDEAF6")
    grid_frame.place(relx=0.5, rely=0.53, anchor="center")

    # Create and arrange buttons
    row = 0
    col = 0
    for name, (img_path, command) in element_buttons.items():
        img = Image.open(img_path).resize((216, 216))
        photo = ImageTk.PhotoImage(img)
        btn = customtkinter.CTkButton(
            grid_frame,
            image=photo,
            text=name,
            compound="top",
            width=256,
            height=256,
            fg_color='#BDEAF6',
            bg_color='#BDEAF6',
            hover_color="black",
            command=command
        )
        btn.image = photo  # Keep a reference
        btn.grid(row=row, column=col, padx=20, pady=10)

        col += 1
        if col > 2:  # 3 columns max
            col = 0
            row += 1

    # Help popup for learn page
    def show_info_popup():
        popup = customtkinter.CTkToplevel(root)
        popup.geometry("900x600")
        popup.title("Information")
        popup.attributes("-topmost", True)

        bg_image = customtkinter.CTkImage(light_image=Image.open("Help_Background.png"), size=(1920, 1080))
        bg_label = customtkinter.CTkLabel(popup, image=bg_image, text="")
        bg_label.image = bg_image 
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        popup_label = customtkinter.CTkLabel(
            popup,
            text=("Click any one of the image to learn more about that element\nAll 6 elements will be tested in the quiz\n"),
            font=("Helvetica", 48), justify="center", text_color="black", fg_color='#82ADFE', wraplength=1000)
        popup_label.place(relx=0.5, rely=0.5, anchor="center")

        close_button = customtkinter.CTkButton(
            popup, text="Close Window ❌", font=("Helvetica", 32), command=popup.destroy)
        close_button.place(relx=0.5, rely=0.85, anchor="center")

    # Help button
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

    # Button to return to main menu
    def go_back():
        root.destroy()
        Main_File.main_page()

    # Style config for back button
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

    # Place back button on screen
    back_button = customtkinter.CTkButton(root, text="Back to Main Menu", command=go_back, **button_config)
    back_button.place(relx=0.5, rely=0.82, anchor="center")

    root.mainloop()