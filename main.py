from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0,END)
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '?', '/']

    password_u_letters = [choice(upper_letters) for _ in range(randint(4,6))]
    password_l_letters= [choice(lower_letters) for _ in range(randint(4,6))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_u_letters + password_l_letters + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_text = web_entry.get()
    email_text=email_entry.get()
    password_text=password_entry.get()

    if len(web_text)==0 or len(email_text)==0 or len(password_text)==0:
        messagebox.showwarning(title="Oops", message="Empty Entry!\nPlease fill all the info correctly.")
    else:
        is_ok=messagebox.askokcancel(title=web_text, message=f"These are the details entered: \nEmail:  {email_text}\nPassword:  {password_text}\n\nDo you want to save it?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"'{web_text}' | '{email_text}' | '{password_text}'\n")
            web_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=40,pady=20)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row=0,column=1,padx=10,pady=10)

website_label= ttk.Label(text= "Website:")
website_label.grid(row=1,column=0,pady=5,sticky="W")

web_entry= ttk.Entry()
web_entry.grid(row=1,column=1,columnspan=2,sticky="EW")
web_entry.focus()

email_label= ttk.Label(text= "Email/Username:")
email_label.grid(row=2,column=0,padx=(0,20),pady=5,sticky="W")

email_entry = ttk.Entry()
email_entry.grid(row=2,column=1,columnspan=2,sticky="EW")

password_label= ttk.Label(text= "Password:")
password_label.grid(row=3,column=0,pady=5,sticky="W")

password_entry = ttk.Entry()
password_entry.grid(row= 3,column=1,sticky="EW")

password_button=ttk.Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2,sticky="EW")

add_button=ttk.Button(text="Add",command=save)
add_button.grid(row=4,column=1,pady=(15,40),columnspan=2,sticky="EW")


window.mainloop()