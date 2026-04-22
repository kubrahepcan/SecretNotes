from tkinter import *
window = Tk()
window.title("Secret Notes")
window.config(bg="light pink")
window.minsize(width=400, height=700)

#First label
title = Label(text="Enter your title", bg="light pink", pady=20, font=15)
title.pack()
#First Entry
entry1 = Entry()
entry1.pack(ipadx=80)
#Second Label
secret = Label(text="Enter your secret", bg="light pink", pady=20, font=15)
secret.pack()
#Second Entry
entry2 = Entry()
entry2.pack(ipadx=80, ipady=80)
#Third label
masterkey = Label(text="Enter your key", bg="light pink", pady=20, font=15)
masterkey.pack()
#Third Entry
entry3 = Entry()
entry3.pack(ipadx=80)
#Save Button
button = Button(text="Save & Encrypt")
button.pack(pady=20)
#Decrypt Button
button2 = Button(text="Decrypt")
button2.pack(pady=5)

window.mainloop()