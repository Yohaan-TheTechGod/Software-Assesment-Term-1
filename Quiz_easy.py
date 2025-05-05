from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import quiz_page    # Allow code to open to this file

def start_quiz():   
    # Read questions from the file
    with open("Quiz_easy.txt", "r") as file:
        questions = file.readlines()

    quiz_data = []
    for q in questions:
        if not q.strip().startswith("#"):  # Ignore comments
            data = q.strip().split(";")
            quiz_data.append({
                "question": data[0],    # Extract questions
                "options": data[1:-1],  # Extract options
                "answer": data[-1]      # Extract correct answer
            })
    
    class QuizApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Quiz Easy")
        
            self.score = 0
            self.current_question_index = 0
            self.time_left = 15  # 15-second timer
            self.timer_id = None  # ID for tracking the active timer callback

            # Set background image
            self.bg_image = ImageTk.PhotoImage(Image.open("Quiz_Background.png").resize((1920, 1080)))
            self.bg_label = tk.Label(root, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            # UI elements directly placed on root (no frame)
            self.question_label = tk.Label(root, text="", wraplength=1200, font=("Arial", 32, "bold"), fg="black", bg="white", justify="center")
            self.question_label.place(relx=0.5, rely=0.2, anchor="center")
        
            self.option_buttons = []
            for i in range(4):  # Create 4 buttons for multiple-choice options
                btn = tk.Button(root, text="", width=40, height=2, font=("Arial", 24), 
                                command=lambda i=i: self.check_answer(i), 
                                bg="#ADD8E6", activebackground="#87CEEB")
                btn.place(relx=0.5, rely=0.35 + i * 0.12, anchor="center")
                self.option_buttons.append(btn)
        
            self.timer_label = tk.Label(root, text=f"Time left: {self.time_left} seconds", font=("Arial", 24, "italic"), fg="black", bg="#FAFAFA")
            self.timer_label.place(relx=0.5, rely=0.8, anchor="center")
        
            self.next_question()

            # Red Cross Button in top-right corner to qut the quiz if necessary, and to go back to quiz_page.py 
            self.close_button = tk.Button(root, text="❌", font=("Arial", 32), command=self.return_to_main, 
                                          fg="red", bg="white", relief="flat", width=3, height=1)
            self.close_button.place(x=1645, y=86) # Placing the button where I want it to be
        
        def update_timer(self):
            # Update the timer label
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            if self.time_left > 0:
                self.time_left -= 1
                self.timer_id = self.root.after(1000, self.update_timer)  # Call this function every 1 second
            else:
                # Time's up, move to the next question message
                messagebox.showinfo("Time's Up", "You ran out of time!")
                self.current_question_index += 1
                self.next_question()
                
        def next_question(self):
            # Cancel any previous timer before starting a new one, making sure always starting from 15 seconds
            if self.timer_id is not None:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None

            if self.current_question_index < len(quiz_data):
                # Reset timer
                self.time_left = 15
                self.update_timer()
            
                # Display the current question and options
                question_data = quiz_data[self.current_question_index]
                self.question_label.config(text=question_data["question"])
                for i, option in enumerate(question_data["options"]):
                    self.option_buttons[i].config(text=option, state="normal")
            else:
                # End of the quiz
                self.show_score_and_exit()
    
        def check_answer(self, selected_index):
            question_data = quiz_data[self.current_question_index]
            correct_option = question_data["answer"]
            selected_option = chr(65 + selected_index)  # Convert index to A, B, C, D
        
            if selected_option == correct_option:
                self.score += 1
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo("Result", f"Incorrect! The correct answer was: {correct_option}")
        
            self.current_question_index += 1
            self.next_question()

        def show_score_and_exit(self):
            # Show the final score and return to quiz_page.py
            result = messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(quiz_data)}")
            if result == "ok":
                self.return_to_main()

        def return_to_main(self):
            self.root.destroy()  # Close the current window
            quiz_page.quiz_page()  # Open quiz_page.py

    # Initialize the application
    root = tk.Tk()
    app = QuizApp(root)

    root.attributes("-fullscreen", True)  # Make the program open fullscreen
    root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))  # Allow exiting fullscreen
    root.mainloop()
