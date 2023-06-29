from tkinter import *
from tkinter import messagebox
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
email_entry = Entry(width=43)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"abc@xyz.com")
password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)
# Button
generate_button =Button(text="Generate")
generate_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()