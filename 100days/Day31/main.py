from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

if __name__ == '__main__':


    window = Tk()
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.title("FlashCards")

    canvas = Canvas(height=526, width=800) 
    front_img = PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=front_img)
    canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) 
    canvas.grid(row=0, column=0, columnspan=2)

    #Labels
#    french_title_label = Label(text="French", fg="black", bg='white', font=("Arial", 40, "italic"))
#    french_title_label.grid(row=0, column=0, sticky=N, pady=150, columnspan=2)
#    english_title_label = Label(text="trouve", fg="black", bg='white', font=("Arial", 60, "bold"))
#    english_title_label.grid(row=0, column=0, sticky=N, pady=263, columnspan=2)

    #Buttons

    right_img = PhotoImage(file="images/right.png") 
    wrong_img = PhotoImage(file="images/wrong.png") 
    wrong_button = Button(image=right_img, highlightthickness=0)
    wrong_button.grid(row=1, column=0) 
    right_button = Button(image=wrong_img, highlightthickness=0)
    right_button.grid(row=1, column=1) 
    
    
    window.mainloop()