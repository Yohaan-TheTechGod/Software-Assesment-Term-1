import tkinter as tk
from tkinter import messagebox

def start_quiz():
    # Read questions from the file
    with open("Quiz_easy.txt", "r") as file:
        questions = file.readlines()
    
    quiz_data = []
    for q in questions:
        if not q.strip().startswith("#"):  # Ignore comments
            data = q.strip().split(";")
            quiz_data.append({
                "question": data[0],
                "options": data[1:-1],  # Extract options
                "answer": data[-1]      # Extract correct answer
            })
    
    class QuizApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Quiz Game")
        
            self.score = 0
            self.current_question_index = 0
            self.time_left = 15  # 15-second timer
        
            # UI elements
            self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
            self.question_label.pack(pady=20)
        
            self.option_buttons = []
            for i in range(4):  # Create 4 buttons for multiple-choice options
                btn = tk.Button(root, text="", width=30, font=("Arial", 12), command=lambda i=i: self.check_answer(i))
                btn.pack(pady=5)
                self.option_buttons.append(btn)
        
            self.timer_label = tk.Label(root, text=f"Time left: {self.time_left} seconds", font=("Arial", 12))
            self.timer_label.pack(pady=10)
        
            self.next_question()
    
        def next_question(self):
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
                messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(quiz_data)}")
                self.root.quit()
    
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
    
        def update_timer(self):
            if self.time_left > 0:
                self.timer_label.config(text=f"Time left: {self.time_left} seconds")
                self.time_left -= 1
                self.root.after(1000, self.update_timer)  # Call this function every 1 second
            else:
                # Time's up, move to the next question
                messagebox.showinfo("Time's Up", "You ran out of time!")
                self.current_question_index += 1
                self.next_question()
    
    # Initialize the application
    root = tk.Tk()
    app = QuizApp(root)

    root.attributes("-fullscreen", True) # Make the program open fullscreen
    root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False)) # Allow the user to escape the fullscreen using Esc key
    root.mainloop()