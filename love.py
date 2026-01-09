import tkinter as tk
from tkinter import ttk
import time
import threading


def calculate_love(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    
    common_letters = set(name1) & set(name2)
    common_score = len(common_letters) * 10

  
    length_diff = abs(len(name1) - len(name2))
    length_score = max(0, 30 - length_diff * 3)

   
    ascii_score = (sum(ord(c) for c in name1 + name2)) % 30

    love_percentage = common_score + length_score + ascii_score

    return min(100, max(5, love_percentage))


def start_calculation():
    name1 = male_entry.get().strip()
    name2 = female_entry.get().strip()

    if not name1 or not name2:
        result_label.config(text="Please enter both names 💔", fg="red")
        return

    result_label.config(text="Calculating Love... 💕", fg="#ff1493")
    progress['value'] = 0
    percent_label.config(text="0%")

    def animate():
        target = calculate_love(name1, name2)

        for i in range(target + 1):
            time.sleep(0.03)
            progress['value'] = i
            percent_label.config(text=f"{i}%")
            root.update_idletasks()

        if target >= 85:
            msg = "Perfect Match 💍❤️"
        elif target >= 65:
            msg = "Strong Love 💖"
        elif target >= 45:
            msg = "Average Match 🙂"
        else:
            msg = "Needs Effort 💔"

        result_label.config(
            text=f"Love Percentage: {target}%\n{msg}",
            fg="#e60073"
        )

    threading.Thread(target=animate, daemon=True).start()


root = tk.Tk()
root.title("💖 Love Calculator")
root.geometry("420x520")
root.configure(bg="#fff0f5")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TProgressbar",
    thickness=20,
    troughcolor="#ffd6e8",
    background="#ff1493"
)


title = tk.Label(
    root,
    text="💘 Love Calculator 💘",
    font=("Comic Sans MS", 22, "bold"),
    bg="#fff0f5",
    fg="#ff1493"
)
title.pack(pady=20)


frame = tk.Frame(root, bg="#fff0f5")
frame.pack(pady=10)

tk.Label(frame, text="Male Name 👨", font=("Arial", 12), bg="#fff0f5").pack(pady=5)
male_entry = tk.Entry(frame, font=("Arial", 14), width=25)
male_entry.pack(pady=5)

tk.Label(frame, text="Female Name 👩", font=("Arial", 12), bg="#fff0f5").pack(pady=5)
female_entry = tk.Entry(frame, font=("Arial", 14), width=25)
female_entry.pack(pady=5)


calc_btn = tk.Button(
    root,
    text="💗 Calculate Love 💗",
    font=("Arial", 14, "bold"),
    bg="#ff1493",
    fg="white",
    padx=10,
    pady=5,
    command=start_calculation
)
calc_btn.pack(pady=20)


progress = ttk.Progressbar(root, length=300, maximum=100)
progress.pack(pady=10)

percent_label = tk.Label(
    root,
    text="0%",
    font=("Arial", 16, "bold"),
    bg="#fff0f5",
    fg="#ff1493"
)
percent_label.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#fff0f5",
    fg="#e60073",
    justify="center",
    anchor="center"
)
result_label.pack(pady=20)


root.mainloop()
