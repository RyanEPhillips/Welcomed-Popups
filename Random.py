import random
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

messages = [
    "1"
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]

images = [
    "1.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg",
    "7.jpg",
    "8.jpg",
    "9.jpg",
    "10.jpg"
]


def show_me(msg):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Message", msg)

    msg = random.choice(messages)
    img_path = random.choice(images)

    img = Image.open(img_path)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)

    label_img = tk.Label(root, image=photo)
    label_img.pack()

    label_text = tk.Label(root, text=msg, font=("Arial", 14))
    label_text.pack()

    button = tk.Button(root, text="Close", command=root.destroy)
    button.pack()

    time.sleep(5)  # Keep the message box open for 5 seconds
    root.destroy()  # Close the message box after displaying

    root.mainloop()

while True:
    wait_time = random.randint(600, 3600)  # 10–60 minutes
    time.sleep(wait_time)
    show_me()

