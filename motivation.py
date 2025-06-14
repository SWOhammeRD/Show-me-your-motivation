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

    popup = tk.Tk()
    popup.title("Your Motivation")
    popup.geometry("400x200")
    popup.configure(bg="#1e2a38")

    # Prevent resizing
    popup.resizable(False, False)

    # Center the window on screen
    popup.update_idletasks()
    w = popup.winfo_screenwidth()
    h = popup.winfo_screenheight()
    x = (w // 2) - 200
    y = (h // 2) - 100
    popup.geometry(f"+{x}+{y}")

    # Display the quote
    tk.Label(popup, text="💡 Your Motivation",
             bg="#1e2a38", fg="#e0e0e0", font=("Segoe UI", 14, "bold")).pack(pady=(20, 5))

    tk.Label(popup, text=quote, wraplength=350,
             bg="#1e2a38", fg="#e0e0e0", font=("Segoe UI", 11)).pack(pady=5)

    tk.Button(popup, text="OK", command=popup.destroy,
              font=("Segoe UI", 11, "bold"),
              bg="#2d82b5", fg="white", activebackground="#246b94",
              relief="flat", padx=15, pady=6).pack(pady=20)

    popup.mainloop()
    sys.exit(0)

def open_quote_editor():
    editor = tk.Tk()
    editor.title("Edit Your Quotes (Max 5)")
    editor.geometry("500x340")
    editor.configure(bg="#1e2a38")

    quotes = load_quotes()
    entries = []

    def save_and_close():
        new_quotes = [entry.get().strip() for entry in entries if entry.get().strip()]
        save_quotes(new_quotes)
        messagebox.showinfo("Saved", "Quotes updated successfully.")
        editor.destroy()

    tk.Label(editor, text="Edit Your Motivational Quotes",
             bg="#1e2a38", fg="#e0e0e0", font=("Segoe UI", 14, "bold")).pack(pady=(20, 10))

    for i in range(5):
        entry = tk.Entry(editor, width=60, font=("Segoe UI", 11),
                         bg="#354a5f", fg="#e0e0e0", insertbackground="#e0e0e0",
                         relief="flat", highlightthickness=1,
                         highlightbackground="#2d82b5", highlightcolor="#2d82b5")
        if i < len(quotes):
            entry.insert(0, quotes[i])
        entry.pack(pady=6, padx=10)
        entries.append(entry)

    tk.Button(editor, text="💾 Save Quotes", font=("Segoe UI", 11, "bold"),
              bg="#2d82b5", fg="white", activebackground="#246b94",
              relief="flat", padx=15, pady=6, command=save_and_close).pack(pady=20)

    editor.mainloop()

# === Entry point ===
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--popup":
        show_random_quote()
    else:
        open_quote_editor()
