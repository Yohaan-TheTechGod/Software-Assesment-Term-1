import customtkinter
from tkinter import Toplevel
from PIL import Image, ImageTk
import Main_File 

def learn_page():
    root = customtkinter.CTk()
    root.title("Learning Page")
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

    bg_image = Image.open("background.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = customtkinter.CTkLabel(root, image=bg_photo, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    header = customtkinter.CTkLabel(root, text="Learn all about these Alkali Metals", font=("Helvetica", 36, "bold"), text_color="white", bg_color="black")
    header.pack(pady=30)

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
        info_window = Toplevel(root)
        info_window.title(element_name)
        info_window.geometry("500x400")
        info_label = customtkinter.CTkLabel(info_window, text=f"{element_name}\n\n{element_info}", font=("Helvetica", 16), justify="center", wraplength=400)
        info_label.pack(expand=True, pady=20)

    grid_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    grid_frame.pack(pady=10)

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
            width=150,
            height=150,
            fg_color="transparent",
            hover_color="#444444",
            command=lambda e=element, i=info: show_element_info(e, i)
        )
        btn.image = photo
        btn.grid(row=row, column=col, padx=40, pady=20)

        col += 1
        if col > 2:
            col = 0
            row += 1

    def go_back():
        root.destroy()
        Main_File.main_page()

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

    back_button = customtkinter.CTkButton(root, text="Back to Main Menu", command=go_back, **button_config)
    back_button.pack(pady=30)

    root.mainloop()
