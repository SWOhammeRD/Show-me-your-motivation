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
    popup.overrideredirect(True)
    popup.attributes("-topmost", True)
    popup.configure(bg="#000000")  # creates an outer border feel

    # Dimensions
    width, height = 620, 260
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    final_x = (screen_width - width) // 2
    final_y = (screen_height - height) // 2

    popup.geometry(f"{width}x{height}+{final_x}+{final_y + 50}")

    # Main frame inside the popup
    frame = tk.Frame(popup, bg="#1e2a38", bd=2, relief="flat", highlightthickness=2, highlightbackground="#2d82b5")
    frame.pack(expand=True, fill="both", padx=4, pady=4)

    # Header
    tk.Label(frame, text="⚡ Your Motivation",
             bg="#1e2a38", fg="#e0e0e0",
             font=("Segoe UI", 20, "bold")).pack(pady=(20, 10))

    # Quote Text
    tk.Label(frame, text=quote, wraplength=560, justify="center",
             bg="#1e2a38", fg="#e0e0e0",
             font=("Segoe UI", 16)).pack(pady=(0, 15))

    # OK button
    tk.Button(frame, text="OK", command=popup.destroy,
              font=("Segoe UI", 12, "bold"), bg="#2d82b5", fg="white",
              activebackground="#246b94", relief="flat",
              padx=14, pady=6).pack()

    # Slide-up animation
    def animate_up(y):
        if y > final_y:
            y -= 4
            popup.geometry(f"{width}x{height}+{final_x}+{y}")
            popup.after(5, lambda: animate_up(y))
        else:
            popup.geometry(f"{width}x{height}+{final_x}+{final_y}")

    animate_up(final_y + 50)

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

    # Header
    tk.Label(editor, text="Edit Your Motivational Quotes",
             bg="#1e2a38", fg="#e0e0e0", font=("Segoe UI", 14, "bold")).pack(pady=(20, 10))

    # Hover effect handlers
    def on_enter(e):
        e.widget.config(bg="#3f5a70")  # lighter on hover

    def on_leave(e):
        e.widget.config(bg="#354a5f")  # default color

    # Entry fields with hover
    for i in range(5):
        entry = tk.Entry(editor, width=60, font=("Segoe UI", 11),
                         bg="#354a5f", fg="#e0e0e0", insertbackground="#e0e0e0",
                         relief="flat", highlightthickness=1,
                         highlightbackground="#2d82b5", highlightcolor="#2d82b5")
        if i < len(quotes):
            entry.insert(0, quotes[i])
        entry.pack(pady=6, padx=10)
        entry.bind("<Enter>", on_enter)
        entry.bind("<Leave>", on_leave)
        entries.append(entry)

    # Save button
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
