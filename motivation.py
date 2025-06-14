import tkinter as tk
from tkinter import messagebox
import json
import os
import random
import sys

# File to store up to 5 quotes
QUOTE_FILE = "quotes.json"

# Load quotes from JSON file or create it if missing/corrupted
def load_quotes():
    if not os.path.exists(QUOTE_FILE):
        with open(QUOTE_FILE, 'w') as f:
            json.dump({"quotes": []}, f)

    try:
        with open(QUOTE_FILE, 'r') as f:
            data = json.load(f)
            return data.get("quotes", [])
    except json.JSONDecodeError:
        # If file is corrupt/empty, reset it
        with open(QUOTE_FILE, 'w') as f:
            json.dump({"quotes": []}, f)
        return []

# Save quotes to JSON file (limit to 5)
def save_quotes(quotes):
    with open(QUOTE_FILE, 'w') as f:
        json.dump({"quotes": quotes[:5]}, f)

# Show a random quote in a messagebox
def show_random_quote():
    quotes = load_quotes()
    if quotes:
        quote = random.choice(quotes)
    else:
        quote = "No quotes saved yet. Open the app manually to add some!"
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Your Motivation", quote)
    root.destroy()

# GUI to manually edit up to 5 quotes
def open_quote_editor():
    quotes = load_quotes()

    editor = tk.Tk()
    editor.title("Edit Your Quotes (Max 5)")
    editor.geometry("500x300")

    entries = []

    def save_and_close():
        new_quotes = [entry.get().strip() for entry in entries if entry.get().strip()]
        save_quotes(new_quotes)
        messagebox.showinfo("Saved", "Quotes updated successfully.")
        editor.destroy()

    for i in range(5):
        entry = tk.Entry(editor, width=70)
        if i < len(quotes):
            entry.insert(0, quotes[i])
        entry.pack(pady=5)
        entries.append(entry)

    save_btn = tk.Button(editor, text="Save Quotes", command=save_and_close)
    save_btn.pack(pady=15)

    editor.mainloop()

# Entry point
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--popup":
        show_random_quote()
    else:
        open_quote_editor()
