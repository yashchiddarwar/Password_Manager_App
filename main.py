from tkinter import *
from tkinter import messagebox as mb
import random
import pyperclip
from pandas import *
import json

FONT_NAME = "Courier"
OPTIONS = ["chiddarwaryash99@gmail.com", "rememberyash99@gmail.com", "itsmeyash2909@gmail.com", "mranonymous43@protonmail.com"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwd_gen():
    passentry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(1, 2)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(numbers) for _ in range(nr_numbers)]
    number_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    passentry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def tranfer_data():
    website = webentry.get()

    #Used the variable assigned to the option menu in order to retrieve the data.
    email = variable.get()

    password = passentry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        mb.showerror(title="Error", message="Don't leave any field empty!")
    else:
        confirmation = mb.askokcancel(title=website,
                                  message=f"You have entered the following details:\nEmail: {email}\nPassword: {password}\nPress ok to confirm entry!")
    if confirmation:
        try:
            with open("datatext.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("datatext.json", "w") as file:
                json.dump(new_data, file, indent=4)
                webentry.delete(0, END)
                passentry.delete(0, END)
        else:
            with open("datatext.json", "w") as file:
                json.dump(data, file, indent=4)
                webentry.delete(0, END)
                passentry.delete(0, END)

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_data():
    search_key = webentry.get()
    with open("datatext.json","r") as file:
        check_data = json.load(file)
        if search_key in check_data:
            # print(check_data[search_key]["email"])
            # print(check_data[search_key]["password"])
            new_alert = mb.showinfo("Login details",f"Username: {check_data[search_key]['email']}\nPassword: {check_data[search_key]['password']}")
        else:
            mb.showerror("Website entry not found.","Entered website has no passwords in the database!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(width=10, height=1, text="Website:", font=(FONT_NAME, 10))
website.grid(row=1, column=0)



username = Label(width=20, height=1, text="Email/Username:", font=(FONT_NAME, 10))
username.grid(row=2, column=0)

password = Label(width=20, height=1, text="Password:", font=(FONT_NAME, 10))
password.grid(row=3, column=0)

webentry = Entry(width=33)
webentry.grid(row=1, column=1)
webentry.focus()

search = Button(width=23, height=1, text="Search", font=(FONT_NAME, 10),command=search_data)
search.grid(row=1, column=2, columnspan=2)

# usernameentry = Entry(width=65)
# usernameentry.grid(row=2, column=1, columnspan=2)
variable = StringVar(window)
variable.set(OPTIONS[0])
usernameentry = OptionMenu(window, variable, *OPTIONS)
usernameentry.grid(row=2, column=1, columnspan=2)
usernameentry.config(width=60)

passentry = Entry(width=33)
passentry.grid(row=3, column=1)

generate = Button(text="Generate", width=26, command=pwd_gen)
generate.grid(row=3, column=2, columnspan=2)

add = Button(text="Add", width=55, command=tranfer_data)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
