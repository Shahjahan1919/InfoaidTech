import tkinter as tk
from tkinter import simpledialog, messagebox, font
import random

class GuessingGame:
    def __init__(self, master):
        # Colors
        self.bg_color = "#F0FFF0" 
        self.fg_color = "#C71585"  
        self.accent_color = "#000000"  
        self.button_bg = "#FFFFFF"  
        self.button_fg = "#556B2F"  

        # Main Window Configuration
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("600x500")
        self.master.configure(bg=self.bg_color)
        self.master.resizable(False, False)

        self.init_welcome()

    def init_welcome(self):
        # Font
        self.font_large = font.Font(family="Arial", size=20, weight="bold")
        self.font_medium = font.Font(family="Arial", size=16)

        self.welcome_label = tk.Label(self.master, text="Welcome to the Guessing Game!", font=self.font_large,  bg=self.bg_color, fg=self.fg_color)
        self.welcome_label.pack(pady=60)

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game, width=15, bg=self.button_bg, fg=self.button_fg, font=self.font_medium, relief=tk.FLAT, borderwidth=0, activebackground=self.accent_color, activeforeground=self.fg_color)
        self.start_button.pack(pady=40)

    def start_game(self):
        self.name = simpledialog.askstring("Name", "Please enter your name:")
        self.welcome_label.destroy()
        self.start_button.destroy()

        self.title_label = tk.Label(self.master, text=f"Hello, {self.name}! Guess a number between 1 and 100.", font=self.font_medium, bg=self.bg_color, fg=self.fg_color)
        self.title_label.pack(pady=20)

        self.entry = tk.Entry(self.master, font=self.font_medium, relief=tk.FLAT, fg=self.accent_color, bg=self.button_bg)
        self.entry.pack(pady=20)

        self.feedback_label = tk.Label(self.master, text="", font=self.font_medium, bg=self.bg_color, fg=self.accent_color)
        self.feedback_label.pack(pady=10)

        self.button_frame = tk.Frame(self.master, bg=self.bg_color)
        self.button_frame.pack(pady=20)

        self.guess_button = tk.Button(self.button_frame, text="Guess", command=self.check_guess, width=10, bg=self.button_bg, fg=self.fg_color, font=self.font_medium, relief=tk.FLAT, borderwidth=0, activebackground=self.accent_color, activeforeground=self.fg_color)
        self.guess_button.grid(row=0, column=0, padx=10)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.master.quit, width=10, bg=self.button_bg, fg=self.fg_color, font=self.font_medium, relief=tk.FLAT, borderwidth=0, activebackground=self.accent_color, activeforeground=self.fg_color)
        self.quit_button.grid(row=0, column=1, padx=10)

        self.reset()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess == self.target_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.play_again()
            elif guess < self.target_number:
                self.feedback_label.config(text=f"Too low! Attempts left: {10 - self.attempts}")
            else:
                self.feedback_label.config(text=f"Too high! Attempts left: {10 - self.attempts}")
            if self.attempts >= 10:
                messagebox.showinfo("Game Over", f"You've used up your attempts! The number was {self.target_number}.")
                self.play_again()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def play_again(self):
        choice = messagebox.askyesno("Play Again?", "Would you like to play again?")
        if choice:
            self.reset()
        else:
            self.master.quit()

    def reset(self):
        self.attempts = 0
        self.target_number = random.randint(1, 100)
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
