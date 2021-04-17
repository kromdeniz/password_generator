from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD FINDER ------------------------------- #


def find_pass():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)#json as a dict
    except FileNotFoundError:
        messagebox.showerror("Oops", "No data file found")
    else:
        if website in data:

            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=website, message=f"{email} \n{password}")
            pyperclip.copy(password)
        else:
            messagebox.showwarning("Oops", f"No data exist for {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for letter in range(randint(8, 10))]
    random_numbers = [choice(numbers) for num in range(randint(2, 4))]
    random_symbols = [choice(symbols) for sym in range(randint(2, 4))]

    passwords_list = random_letters + random_numbers + random_symbols
    shuffle(passwords_list)
    password = "".join(passwords_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        # confirm = messagebox.askokcancel(website.title(), f"Email: {email}\nPassword: {password}\nDo you want to save?")
        # if confirm:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                # creates a dict from json file
                data.update(new_data)
                # updates the dict data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                # writes the updated dict data to the file
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, padx=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=43)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kromdeniz@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

find_button = Button(text="Find", command=find_pass)
find_button.grid(row=1, column=2, sticky="E")

window.mainloop()

