from tkinter import *
from tkinter import messagebox
import pyperclip
import random
"""
Keepass, Kepass, kepass, keepass, password management, Password Management
-title titleString
Specifies a string to display as the title of the message box. This option is ignored on Mac OS X, where platform guidelines forbid the use of a title on this kind of dialog."""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genPass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    password_list_let = []
    password_list_sym = [] 
    password_list_num = []

    password_list_let = [random.choice(letters) for _ in range(nr_letters)]
#    for char in range(nr_letters):
#      password_list.append(random.choice(letters))
    password_list_sym = [random.choice(symbols) for _ in range(nr_symbols)]
#    for char in range(nr_symbols):
#      password_list += random.choice(symbols)
    password_list_num = [random.choice(numbers) for _ in range(nr_numbers)]
#    for char in range(nr_numbers):
#      password_list += random.choice(numbers)
    
    password_list = password_list_let + password_list_num + password_list_sym 
    random.shuffle(password_list)
    
    password = "".join(password_list)
#    password = ""
#    for char in password_list:
#      password += char
    print(password)
#    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_uname_entry.get()
    passw = pass_entry.get()
    if len(website) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops", message="Cannot enter blank fields!") 
    else:
        ok_to_save = messagebox.askokcancel(title=f"{website}", message=f"\nEntered following info: \n Website: {website}"
                f"\ne-mail: {email}" 
                f"\npassword: {passw}")
        if ok_to_save:
            with open("data.txt", "at") as data:
                data.write(f"{website_entry.get()} | {email_uname_entry.get()} | {pass_entry.get()}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)
#window.minsize(200, 200)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

#Website label and textbox
website_label = Label(text="Website", font = ("Aerial", 12, "normal"), highlightthickness=0)
website_label.grid(column=0, row=1)

website_var = StringVar()
website_entry = Entry(width=35, textvariable=website_var)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# "Email/Username" label and textbox
email_uname_label = Label(text="Email/Username", font = ("Aerial", 12, "normal"), highlightthickness=0)
email_uname_label.grid(column=0, row=2)

email_uname_entry = Entry(width=35)
email_uname_entry.insert(END, string="")
email_uname_entry.grid(column=1, row=2, columnspan=2)
email_uname_entry.insert(0, 'slaanjoo@gmail.com')

# "Password label"/textbox
pass_label = Label(text="Password", font = ("Aerial", 12, "normal"), highlightthickness=0)
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=21)
pass_entry.insert(END, string="")
passw = pass_entry.get()
pass_entry.grid(column=1, row=3)

# "Generate password" button
gen_pass = Button(text="Generate Password", width=13, font=("Aerial", 11, "normal"), command = genPass)
gen_pass.grid(column=2, row=3)

#"Add" button
add_button = Button(text="Add", width=36, font=("Aerial", 12, "normal"), command=save)
add_button.grid(column=1, row=4, columnspan=36)

window.mainloop()