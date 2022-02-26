from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("data/french_words.csv")
lista = df.to_dict(orient="records")

def show_word():
    canvas.itemconfigure(canvas_image, image=front_img)
    title.set("French")
    french_word = random.choice(lista) 
    fr_word.set(f"{french_word['French']}")
    print(f'French: {french_word["French"]} ----> English: {french_word["English"]}') 
    window.after(3000, flip)

def flip():
    canvas.itemconfigure(canvas_image, image=back_img)
    frankish = fr_word.get()
    title.set("English")
    print(fr_word.get())
    for french in lista: 
        if french['French'] ==  frankish:
            fr_word.set(french['English'])
    print(fr_word.get())
    

if __name__ == '__main__':


    window = Tk()
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.title("FlashCards")
    
    canvas = Canvas(height=526, width=800) 
    front_img = PhotoImage(file="images/card_front.png")
    back_img = PhotoImage(file="images/card_back.png")
    canvas_image = canvas.create_image(400, 263, image=front_img)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) 
    canvas.grid(row=0, column=0, columnspan=2)

    #Labels
    fr_word = StringVar()
    title = StringVar()
    title.set("French")
    title_label = Label(textvariable=title, fg="black", bg='white', font=("Arial", 40, "italic"))
    title_label.grid(row=0, column=0, sticky=N, pady=150, columnspan=2)
    title_label.update()

    word_label = Label(text="trouve", textvariable=fr_word, fg="black", bg='white', font=("Arial", 60, "bold"))
    word_label.grid(row=0, column=0, sticky=N, pady=263, columnspan=2)
    word_label.update()
    
    #Buttons
    
    wrong_img = PhotoImage(file="images/wrong.png") 
    wrong_button = Button(image=wrong_img, highlightthickness=0, command=show_word)
    wrong_button.grid(row=1, column=0) 
    
    right_img = PhotoImage(file="images/right.png") 
    right_button = Button(image=right_img, highlightthickness=0, command=show_word)
    right_button.grid(row=1, column=1) 
    
#    window.after(3000, flip)
    
    window.mainloop()