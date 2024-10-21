import tkinter as tk
from tkinter import messagebox
import random


def show_popup():
    # List of quotes, you can add as much as you want
    quotes = [
        ""
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

