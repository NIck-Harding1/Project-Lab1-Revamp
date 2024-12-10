import tkinter as tk
from tkinter import messagebox
from logic import VotingLogic

class VotingApp:
    def __init__(self):
        self.logic = VotingLogic()
        self.root = tk.Tk()
        self.root.title("Voting Application")
        self.root.geometry("300x300")  # Increase the size of the window

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="VOTING APPLICATION").pack(pady=10)

        tk.Label(self.root, text="ID").pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack(pady=5)

        tk.Label(self.root, text="CANDIDATES").pack()
        self.candidate_var = tk.StringVar()
        tk.Radiobutton(self.root, text="Jane", variable=self.candidate_var, value="Jane").pack()
        tk.Radiobutton(self.root, text="John", variable=self.candidate_var, value="John").pack()

        self.submit_button = tk.Button(self.root, text="SUBMIT VOTE", command=self.submit_vote)
        self.submit_button.pack(pady=10)

        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.pack(pady=5)

    def submit_vote(self):
        voter_id = self.id_entry.get().strip()
        candidate = self.candidate_var.get()

        if not voter_id:
            messagebox.showerror("Error", "ID cannot be empty")
            return

        if not candidate:
            messagebox.showerror("Error", "Please select a candidate")
            return

        if self.logic.has_voted(voter_id):
            self.message_label.config(text="Already Voted")
        else:
            self.logic.record_vote(voter_id, candidate)
            self.message_label.config(text="Vote Submitted")

    def run(self):
        self.root.mainloop()
