from tkinter import *

#create labels - "Miles", "is equal to", "Km", display calculation label , an entry box, and a button

def calculate():
    print("Clicked =====")
    new_text = float(input.get()) * 1.60934
    result.config(text=f"{new_text}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

#Label miles
miles = Label(text="Miles")
miles.grid(column=2, row=0)

#Label "is equal to"
is_equal_to = Label(text="is equal to  ")
is_equal_to.grid(row=1, column=0)

#Label "Km"
km = Label(text="km")
km.grid(column=2, row=1)

#Label "result"
result = Label(text="RESULT")
result.grid(column=1, row=1)

#button calculate
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()