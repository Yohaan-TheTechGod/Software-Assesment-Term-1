import tkinter as tk

def open_quiz_page(root, open_main_page):

    for widget in root.winfo_children():
        widget.destroy()


    tk.Label(root, text="Quiz Page: In development", font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Back", command=lambda: open_main_page(root)).pack(pady=10)
