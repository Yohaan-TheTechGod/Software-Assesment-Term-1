from tkinter import *
import customtkinter
from tkinter import Toplevel
from PIL import Image, ImageTk
import Main_File 

def learn_page():
    root = customtkinter.CTk()
    root.title("Learning Page")
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    bg = PhotoImage(file='Learn_Background.png')
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    elements = {
        "Lithium": "ADD INFORMATION HERE!!",
        "Sodium": "ADD INFORMATION HERE!!",
        "Potassium": "ADD INFORMATION HERE!!",
        "Rubidium": "ADD INFORMATION HERE!!",
        "Caesium": "ADD INFORMATION HERE!!",
        "Francium": "ADD INFORMATION HERE!!",
    }

    element_images = {
        "Lithium": "Lithium.png",  
        "Sodium": "Sodium.png",
        "Potassium": "Potassium.png",
        "Rubidium": "Rubidium.png",
        "Caesium": "Caesium.png",
        "Francium": "Francium.png",
    }

    def show_element_info(element_name, element_info):
        info_window = customtkinter.CTkToplevel(root)
        info_window.title(element_name)
        info_window.geometry("500x400")
        info_window.configure(fg_color="transparent")
        info_label = customtkinter.CTkLabel(
            info_window,
            text=f"{element_name}\n\n{element_info}",
            font=("Helvetica", 16),
            justify="center",
            wraplength=400,
            fg_color="#BDEAF6",
            bg_color="#BDEAF6"
        )
        info_label.pack(expand=True, pady=20)

    grid_frame = customtkinter.CTkFrame(root, fg_color="#BDEAF6", bg_color="#BDEAF6")
    grid_frame.place(relx=0.5, rely=0.53, anchor="center")

    row = 0
    col = 0
    for index, (element, info) in enumerate(elements.items()):
        img = Image.open(element_images[element]).resize((216, 216))
        photo = ImageTk.PhotoImage(img)
        btn = customtkinter.CTkButton(
            grid_frame,
            image=photo,
            text=element,
            compound="top",
            width=256,
            height=256,
            fg_color='#BDEAF6',
            bg_color='#BDEAF6',
            hover_color="black",
            command=lambda e=element, i=info: show_element_info(e, i)
        )
        btn.image = photo
        btn.grid(row=row, column=col, padx=20, pady=10)

        col += 1
        if col > 2:
            col = 0
            row += 1
    
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
    
    def go_back():
        root.destroy()
        Main_File.main_page()

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

    back_button = customtkinter.CTkButton(root, text="Back to Main Menu", command=go_back, **button_config)
    back_button.place(relx=0.5, rely=0.82, anchor="center")

    root.mainloop()
