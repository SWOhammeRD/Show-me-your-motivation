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

    width, height = 620, 280
    popup = tk.Tk()
    popup.overrideredirect(True)
    popup.attributes("-topmost", True)
    popup.configure(bg="#1e2a38")

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    final_x = (screen_width - width) // 2
    final_y = (screen_height - height) // 2

    popup.geometry(f"{width}x{height}+{final_x}+{final_y + 50}")

    canvas = tk.Canvas(popup, width=width, height=height, bg="#1e2a38", highlightthickness=0)
    canvas.pack()

    canvas.create_text(width // 2, 50, text="⚡ Your Motivation",
                       font=("Segoe UI", 18, "bold"), fill="#ffffff")
    canvas.create_text(width // 2, 120, text=quote,
                       font=("Segoe UI", 14), fill="#e0e0e0", width=540)

    def close_popup():
        popup.destroy()

    btn = tk.Button(popup, text="OK", command=close_popup,
                    font=("Segoe UI", 12, "bold"), bg="#2d82b5", fg="white",
                    activebackground="#246b94", relief="flat", padx=14, pady=6)
    canvas.create_window(width // 2, 210, window=btn)

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
    editor.geometry("600x420")
    editor.configure(bg="#1e2a38")
    editor.resizable(False, False)

    canvas = tk.Canvas(editor, width=600, height=420, bg="#1e2a38", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    quotes = load_quotes()
    entries = []

    def save_and_close():
        new_quotes = [entry.get().strip() for entry in entries if entry.get().strip()]
        save_quotes(new_quotes)
        messagebox.showinfo("Saved", "Quotes updated successfully.")
        editor.destroy()

    canvas.create_text(300, 30, text="Edit Your Motivational Quotes",
                       font=("Segoe UI", 16, "bold"), fill="#e0e0e0")

    for i in range(5):
        entry = tk.Entry(editor, width=45, font=("Segoe UI", 11),
                         bg="#354a5f", fg="#e0e0e0", insertbackground="#e0e0e0",
                         relief="flat", highlightthickness=1,
                         highlightbackground="#2d82b5", highlightcolor="#2d82b5")
        if i < len(quotes):
            entry.insert(0, quotes[i])
        canvas.create_window(300, 80 + i * 50, window=entry)
        entries.append(entry)

    save_btn = tk.Button(editor, text="💾 Save Quotes", font=("Segoe UI", 11, "bold"),
                         bg="#2d82b5", fg="white", activebackground="#246b94",
                         relief="flat", padx=15, pady=6, command=save_and_close)
    canvas.create_window(300, 340, window=save_btn)

    editor.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--popup":
        show_random_quote()
    else:
        open_quote_editor()
