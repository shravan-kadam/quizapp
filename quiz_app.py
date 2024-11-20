import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        # Initialize the root window
        self.root = root
        self.root.title("Quiz App")
        
        # Define the list of questions, options, and answers
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "George Orwell"], "answer": "Harper Lee"}
        ]
        
        # Initialize score and current question index
        self.score = 0
        self.current_question = 0
        self.user_answers = [None] * len(self.questions)  # Initialize with None for each question

        # Create the question label
        self.question_label = tk.Label(root, text=self.questions[self.current_question]["question"], font=("Arial", 16))
        self.question_label.pack(pady=20)
        
        # Create the buttons for answer options
        self.option_buttons = []
        self.create_option_buttons()

    def create_option_buttons(self):
        """Create the buttons for the current question options."""
        for button in self.option_buttons:
            button.destroy()  # Destroy previous buttons before creating new ones
        
        self.option_buttons = []  # Clear the list of buttons
        for option in self.questions[self.current_question]["options"]:
            button = tk.Button(self.root, text=option, width=20, height=2, command=lambda opt=option: self.select_answer(opt))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def select_answer(self, selected_option):
        # Store the selected answer in the user_answers list
        self.user_answers[self.current_question] = selected_option

        # Highlight only the selected option with light blue
        for button in self.option_buttons:
            if button.cget("text") == selected_option:
                button.config(bg="lightblue")  # Highlight the selected button

        # Disable all the option buttons after an answer is selected
        for button in self.option_buttons:
            button.config(state="disabled")
        
        # Check the current answer and update the score
        if self.user_answers[self.current_question] == self.questions[self.current_question]["answer"]:
            self.score += 1
        
        # Move to the next question after a short delay
        self.root.after(1000, self.update_question)

    def update_question(self):
        # Move to the next question
        self.current_question += 1
        
        # If there are more questions, update the UI for the next question
        if self.current_question < len(self.questions):
            # Reset the button colors and enable the buttons for the next question
            self.create_option_buttons()  # Recreate the buttons with the updated options
            self.question_label.config(text=self.questions[self.current_question]["question"])
        else:
            # If there are no more questions, show results
            self.show_results()

    def show_results(self):
        # Prepare the result message
        result_message = f"Your final score is {self.score}/{len(self.questions)}\n\n"
        result_message += "Correct Answers:\n"
        
        for i, question in enumerate(self.questions):
            correct_answer = question["answer"]
            user_answer = self.user_answers[i]
            result_message += f"Q{i+1}: {question['question']}\n"
            result_message += f"Your Answer: {user_answer}\n"
            result_message += f"Correct Answer: {correct_answer}\n\n"
            
        # Show the results in a message box
        result_message += "Do you want to restart the quiz?"
        restart = messagebox.askyesno("Quiz Over", result_message)

        if restart:
            self.restart_quiz()
        else:
            self.root.quit()

    def restart_quiz(self):
        # Restart the quiz by resetting values
        self.score = 0
        self.current_question = 0
        self.user_answers = [None] * len(self.questions)  # Reset the user answers
        
        # Reset the interface
        self.question_label.config(text=self.questions[self.current_question]["question"])
        self.create_option_buttons()  # Recreate the first question's options
        
        # Enable all buttons for the first question
        for button in self.option_buttons:
            button.config(bg="SystemButtonFace", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
root.mainloop()
