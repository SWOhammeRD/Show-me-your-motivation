import tkinter as tk
from tkinter import messagebox
import random


def show_popup():
    # List of quotes
    quotes = [
        "Now I'm feeling motivated. - Vergil",
        "Nobody makes my fate, but me - Cayde 6",
        "Bury The light Deep Within",
        "You're my favorite. Don't ever forget that - Cayde 6"
    ]

    # Randomly select a quote
    selected_quote = random.choice(quotes)

    # Create popup window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Show Me Your Motivation", selected_quote)
    root.destroy()


if __name__ == "__main__":
    show_popup()

