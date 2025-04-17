import tkinter as tk
from PIL import Image, ImageTk

def open_main_page(root):
    print("Opening main page") 
    for widget in root.winfo_children():
        widget.destroy()

    
    original_image = Image.open("MainPageBackground.png")  
    bg = ImageTk.PhotoImage(original_image)

    
    labelB = tk.Label(root, image=bg)
    labelB.image = bg 
    labelB.place(relwidth=1, relheight=1)

    def resize_image(event):
        resized_image = original_image.resize((event.width, event.height), Image.LANCZOS)
        bg_resized = ImageTk.PhotoImage(resized_image)
        labelB.configure(image=bg_resized)
        labelB.image = bg_resized  # avoid garbage collection

    root.bind("<Configure>", resize_image)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Elements Quiz Program")
    root.geometry("800x600") 

    open_main_page(root)

    root.mainloop()
