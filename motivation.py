import tkinter as tk
from tkinter import messagebox
import json
import os
import random
import sys

QUOTE_FILE = "quotes.json"

def load_quotes():
    if not os.path.exists(QUOTE_FILE) or os.path.getsize(QUOTE_FILE) == 0:
        with open(QUOTE_FILE, 'w') as f:
            json.dump({"quotes": []}, f)

    try:
        with open(QUOTE_FILE, 'r') as f:
            content = f.read().strip()
            if not content:
                raise json.JSONDecodeError("Empty content", "", 0)
            data = json.loads(content)
            return data.get("quotes", [])
    except (json.JSONDecodeError, ValueError):
        with open(QUOTE_FILE, 'w') as f:
            json.dump({"quotes": []}, f)
        return []

def save_quotes(quotes):
    with open(QUOTE_FILE, 'w') as f:
        json.dump({"quotes": quotes[:5]}, f)

def show_random_quote():
    quotes = load_quotes()
    quote = random.choice(quotes) if quotes else "No quotes saved yet. Open the app manually to add some!"
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Your Motivation", quote)
    root.destroy()

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

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--popup":
        show_random_quote()
    else:
        open_quote_editor()
