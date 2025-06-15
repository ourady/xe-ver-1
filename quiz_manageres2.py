import tkinter as tk
from tkinter import ttk

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

        self.quiz_label = tk.Label(self.quiz_frame, text="Espace Quiz", bg='white')
        self.quiz_label.pack(pady=10)

        # Create the Administration tab
        self.admin_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.admin_frame, text='Administration')

        self.admin_label = tk.Label(self.admin_frame, text="Espace Administration", bg='white')
        self.admin_label.pack(pady=10)

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()

