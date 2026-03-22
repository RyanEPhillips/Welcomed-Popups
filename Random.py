import random
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

messages = [
    "You are doing great!",
    "It's a beautiful day!",
    "Keep up the good work!",
    "You're awesome!",
    "Don't give up!",
    "You've got this!",
    "Stay positive!",
    "You are capable!",
    "You are strong!",
    "You are enough!"
]

images = [
    "img/1.jpg",
    "img/2.jpg",
    "img/3.jpg",
    "img/4.png",
    "img/5.png",
    "img/6.jpg",
    "img/7.jpg"
]


def show_message(msg):
    root = tk.Tk()
    root.title("Reminder")

    label = tk.Label(root, text=msg, font=("Times New Roman", 16), padx=20, pady=20)
    label.pack()

    # Auto close after 5 seconds
    root.after(5000, root.destroy)

    root.mainloop()


def show_image(img_path):
    root = tk.Tk()
    root.title("Reminder")

    img = Image.open(img_path)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.image = photo  # keep reference
    label.pack()

    # auto close after 5 seconds
    root.after(5000, root.destroy)

    root.mainloop()


while True:
    wait_time = random.randint(10, 30)
    time.sleep(wait_time)

    choice = random.choice(["message", "image"])

    if choice == "message":
        msg = random.choice(messages)
        show_message(msg)
    else:
        img = random.choice(images)
        show_image(img)