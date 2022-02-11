from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
   with open("data.txt", "at") as data:
       data.write("test")

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

website_entry = Entry(width=35)
website_entry.insert(END, string="")
website = website_entry.get()
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

#Email/Username label and textbox
email_uname_label = Label(text="Email/Username", font = ("Aerial", 12, "normal"), highlightthickness=0)
email_uname_label.grid(column=0, row=2)

email_uname_entry = Entry(width=35)
email_uname_entry.insert(END, string="")
email_uname = email_uname_entry.get()
email_uname_entry.grid(column=1, row=2, columnspan=2)
email_uname_entry.insert(0, 'slaanjoo@gmail.com')
#Password lable/textbox
pass_label = Label(text="Password", font = ("Aerial", 12, "normal"), highlightthickness=0)
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=21)
pass_entry.insert(END, string="")
passw = pass_entry.get()
pass_entry.grid(column=1, row=3)

#Generate password button
gen_pass = Button(text="Generate Password", width=13, font=("Aerial", 11, "normal"))
gen_pass.grid(column=2, row=3)
#Add button
gen_pass = Button(text="Add", width=37, font=("Aerial", 12, "normal"), command=save)
gen_pass.grid(column=1, row=4, columnspan=36)

window.mainloop()