import os
import tkinter as tk
from tkinter import ttk
import webbrowser
import json

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Manager")
        self.geometry("800x600")

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Create the Quiz tab
        self.quiz_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.quiz_frame, text='Quiz')

        # Button to load quizzes
        self.lancer_quiz_button = tk.Button(self.quiz_frame, text="Charger les quiz", command=self.lancer_quiz)
        self.lancer_quiz_button.pack(pady=10)

        # Create the Administration tab
        self.admin_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.admin_frame, text='Administration')

        self.admin_label = tk.Label(self.admin_frame, text="Espace Administration", bg='white')
        self.admin_label.pack(pady=10)

    def lancer_quiz(self):
        self.quiz_app = QuizLoader(self.quiz_frame, "fichierquizz")

class QuizLoader:
    def __init__(self, parent_frame, quiz_folder):
        self.parent_frame = parent_frame
        self.quiz_folder = quiz_folder
        self.quiz_buttons = []
        self.load_quizzes()

    def load_quizzes(self):
        for filename in os.listdir(self.quiz_folder):
            if filename.endswith(".html"):
                button = tk.Button(self.parent_frame, text=f"Ouvrir {filename}", command=lambda f=filename: self.open_quiz(f))
                button.pack(pady=5)
                self.quiz_buttons.append(button)

    def open_quiz(self, filename):
        path = os.path.abspath(os.path.join(self.quiz_folder, filename))
        if os.path.exists(path):
            webbrowser.open(f"file://{path}")
            self.save_result(filename, "user1", 100)  # Résultat fictif

    def save_result(self, quiz_name, user, score):
        result = {"quiz_name": quiz_name, "user": user, "score": score}
        results_file = "quiz_results.json"
        if os.path.exists(results_file):
            with open(results_file, 'r') as file:
                results = json.load(file)
        else:
            results = []
        results.append(result)
        with open(results_file, 'w') as file:
            json.dump(results, file, indent=4)

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()

