from tkinter import messagebox

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FILE_NAME = "french_words.csv"
from tkinter import *
import pandas
import random

selected_word = {}
try:
    word_df = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    word_df = pandas.read_csv("data/words_to_learn.csv")
finally:
    new_word_dictionary = word_df.to_dict(orient='records')


def pick_random_word():
    global selected_word, flip_timer
    window.after_cancel(flip_timer)
    selected_word = random.choice(new_word_dictionary)
    print(selected_word['French'])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=selected_word['French'], fill="black")
    canvas.itemconfig(card_background, image=photo_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=selected_word['English'], fill="white")


def remove_known_cards():
    new_word_dictionary.remove(selected_word)
    pick_random_word()
    data = pd.DataFrame(new_word_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)


# -------------------------------UI DESIGN-------------------------------#
window = Tk()
window.title("Flash card FRENCH/ENGLISH")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)
# Create canvas to place multiple elements on window
canvas = Canvas(width=800, height=526)

# Create photo image
photo_image = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
# Set image on canvas and set the size
card_background = canvas.create_image(400, 263, image=photo_image)

# Create texts on the flash card

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Set size of the grid
canvas.grid(row=0, column=0, columnspan=2)

# Add cross and check buttons on canvas
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=pick_random_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=remove_known_cards)
known_button.grid(row=1, column=1)

pick_random_word()

window.mainloop()
