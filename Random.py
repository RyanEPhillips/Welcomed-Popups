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
    "Stay positive!"
    "You are capable!",
    "You are strong!",
    "You are enough!"
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

    label_text = tk.Label(root, text=msg, font=("Times New Roman", 16))
    label_text.pack()

    button = tk.Button(root, text="Close", command=root.destroy)
    button.pack()

    time.sleep(5)  # Keep the message box open for 5 seconds
    root.destroy()  # Close the message box after displaying

    root.mainloop()

while True:
    wait_time = random.randint(10, 30)
    # wait_time = random.randint(900, 1800) # Random wait time between 15 and 30 minutes (900 to 1800 seconds)
    time.sleep(wait_time)
    show_me(msg=random.choice(messages))

