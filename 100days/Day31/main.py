from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("data/french_words.csv")
lista = df.to_dict(orient="records")

def show_word():
    french_word = random.choice(lista) 
    word = word_label
    print(french_word["French"])
    canvas.config(word) 

if __name__ == '__main__':


    window = Tk()
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.title("FlashCards")
    
    canvas = Canvas(height=526, width=800) 
    front_img = PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=front_img)
    canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) 
    canvas.grid(row=0, column=0, columnspan=2)
 
    #Labels
    title_label = Label(text="French", fg="black", bg='white', font=("Arial", 40, "italic"))
    v = StringVar()
    title_label.grid(row=0, column=0, sticky=N, pady=150, columnspan=2)
    title_label.update()

    word_label = Label(text="trouve", fg="black", bg='white', font=("Arial", 60, "bold"))
    word_label.grid(row=0, column=0, sticky=N, pady=263, columnspan=2)
    word_label.update()
    
    #Buttons
    
    wrong_img = PhotoImage(file="images/wrong.png") 
    wrong_button = Button(image=wrong_img, highlightthickness=0, command=show_word)
    wrong_button.grid(row=1, column=0) 
    
    right_img = PhotoImage(file="images/right.png") 
    right_button = Button(image=right_img, highlightthickness=0, command=show_word)
    right_button.grid(row=1, column=1) 
    
    
    window.mainloop()