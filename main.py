from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
from cryptography.fernet import Fernet

# password generator

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    #print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# save password
writelist=[]
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # check for empty fields:
    if len(website) ==0 or len(username) == 0 or len(password)==0:
        messagebox.showinfo(title= "Ooops!", message = "Please don't leave any empty fields" )
    else:

        # create a pop-up for user to confirm before saving
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Website: {website} \nEmail: {username} \n Password: {password} \n Is it okay to save? ")
        if is_okay:

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password} \n")

                #clear out the form
                website_entry.delete(0, END)
                #username_entry.delete(0, END)
                password_entry.delete(0, END)

# ui setup
window = Tk()
window.title("Password Manager")

canvas = Canvas(width = 200, height = 200, highlightthickness=0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image=lock_img)
window.config(padx=50, pady=50)
canvas.grid(row=0, column=1)

# add fields:
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width = 50)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry=Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "bdc@max.metrea.aero")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry=Entry(width=32)
password_entry.grid(row=3, column=1)

generate_button = Button(text = "Generate Password", command = generate_password)
generate_button.grid(row = 3, column = 2)

add_button = Button(text = "add", width=43, command=save)
add_button.grid(row = 4, column = 1, columnspan=2)

window.mainloop()
