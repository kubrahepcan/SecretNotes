from tkinter import *
from PIL import ImageTk, Image

window = Tk()
#image
image = Image.open("secret2.png").convert("RGBA").resize((100, 100))
img = ImageTk.PhotoImage(image)

image = Label(window, image=img, bg="light pink")
image.pack(pady=20)

window.title("Secret Notes")
window.config(bg="light pink")
window.minsize(width=400, height=700)

#First label
title = Label(text="Enter your title", bg="light pink", font=15)
title.pack()
#First Entry
entry1 = Text(width=40, height=1)
entry1.pack(pady=(0, 20))
#Second Label
secret = Label(text="Enter your secret", bg="light pink", font=15)
secret.pack()
#Second Entry
entry2 = Text(width=40, height=10)
entry2.pack(pady=(0, 20))
#Third label
masterkey = Label(text="Enter your key", bg="light pink", font=15)
masterkey.pack()
#Third Entry
entry3 = Text(width=40, height=1)
entry3.pack(pady=(0, 20))


##########################################
def save_title():
    title = entry1.get()

    with open("Notes.txt", "a") as file:
        file.write(title + "\n")


def save_secret():
    secret = entry2.get()

    with open("Notes.txt", "a") as file:
        file.write(secret + "\n")


def all_entries():
    save_title()
    save_secret()


#Save Button
button = Button(text="Save & Encrypt", command=all_entries)
button.pack(pady=20)
#Decrypt Button
button2 = Button(text="Decrypt")
button2.pack(pady=5)

window.mainloop()
