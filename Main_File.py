import tkinter as tk
import learn_page
import quiz_page
import about_page

def open_main_page(root):
  
    for widget in root.winfo_children():
        widget.destroy()


    tk.Button(root, text="Learn", command=lambda: learn_page.open_learn_page(root, open_main_page), width=15).pack(pady=10)
    tk.Button(root, text="Quiz", command=lambda: quiz_page.open_quiz_page(root, open_main_page), width=15).pack(pady=10)
    tk.Button(root, text="About", command=lambda: about_page.open_about_page(root, open_main_page), width=15).pack(pady=10)


root = tk.Tk()
root.title("Simple Quiz App")
root.geometry("400x300")


open_main_page(root)


root.mainloop()
