from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    _list = [[random.choice(letters) for x in range(nr_letters)],[random.choice(numbers) for x in range(nr_numbers)],[random.choice(symbols) for x in range(nr_symbols)]]
    password_list = [str(i) for sublist in _list for i in sublist]
    password = random.shuffle(password_list)
    password = "".join(password_list)
    if len(password_entry.get())==0:
        password_entry.insert(0,password)
    else:
        password_entry.delete(0,END)
        password_entry.insert(0,password)
# GUI
def delete():
    website_entry.delete(0,END)
    password_entry.delete(0,END)
def save():
    is_okay = messagebox.askokcancel(title=website_entry.get(), message=f"These are the entered details:\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\nProceed?")
    if (len(email_entry.get())==0 or len(password_entry.get())==0 or len(website_entry.get())==0) and is_okay:
        messagebox.showwarning(title="Oops!!",message="Dont leave the fields empty")
    elif is_okay:
        with open("data.txt",mode="a") as f:
            f.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        delete()
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
lock = PhotoImage(file = "lock.png")
canvas.create_image(100,100,image=lock)
canvas.grid(row=0,column=1)
# Labels
website = Label(text="Website:")
website.grid(row=1,column=0)
email = Label(text="Username/Email:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)
# Entry
website_entry = Entry(width=43)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
# ---- field-----
# email_entry = Entry(width=43)
# email_entry.grid(row=2,column=1,columnspan=2)
# email_entry.insert(0,"abc@xyz.com")
# ---- dropdown ----
email_entry = ttk.Combobox(values=["abc@gmail.com","abc@yahoo.com"],width=40)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)
# Button
generate_button =Button(text="Generate",command=generate)
generate_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()