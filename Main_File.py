import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import learn_page
import quiz_page
import about_page

def open_main_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    # Use pillow to load the image
    original_image = Image.open("Add once image made")

    bg_label = tk.Label(root)
    bg_label.place(relwidth=1, relheight=1)

    def resize_bg(event):
        new_width = event.width
        new_height = event.height
        resized = original_image.resize((new_width, new_height), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(resized)
        bg_label.config(image=bg_image)
        bg_label.image = bg_image  

    root.bind("<Configure>", resize_bg)

    # Wanted to use a horizontal frame to keep buttons in center
    button_frame = tk.Frame(root, bg='', padx=10, pady=10)
    button_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Hovering effect on buttons code
    def on_enter(e):
        e.widget.config(relief='raised', bd=4, bg='#d9d9d9')

    def on_leave(e):
        e.widget.config(relief='flat', bd=2, bg='SystemButtonFace')

    # I want buttons with hover effect so added this code
    buttons = [
        ("Learn", lambda: learn_page.open_learn_page(root, open_main_page)),
        ("Quiz", lambda: quiz_page.open_quiz_page(root, open_main_page)),
        ("About", lambda: about_page.open_about_page(root, open_main_page)),
        ("Exit", root.quit)
    ]

    for (text, cmd) in buttons:
        btn = tk.Button(button_frame, text=text, command=cmd, width=15, relief='flat', bd=2)
        btn.pack(side='left', padx=10)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

root = tk.Tk()
root.title("Elements quiz program")
root.geometry("400x300")

open_main_page(root)

root.mainloop()