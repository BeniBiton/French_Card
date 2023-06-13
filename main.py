from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("C:\\Users\\benbi\\OneDrive\\שולחן העבודה\\files\\flash_card_files\\data\\french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)
    flip_timer = window.after(3000, func=flip_timer)


window = Tk()
window.title("falsh the card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front_image = PhotoImage(
    file="C:\\Users\\benbi\\OneDrive\\שולחן העבודה\\files\\flash_card_files\\images\\card_front.png\\")
card_back_image = PhotoImage(
    file="C:\\Users\\benbi\\OneDrive\\שולחן העבודה\\files\\flash_card_files\\images\\card_back.png\\")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Franch", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="C:\\Users\\benbi\\OneDrive\\שולחן העבודה\\files\\flash_card_files\\images\\wrong.png\\")
unknow_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknow_button.grid(row=1, column=0)

check_image = PhotoImage(file="C:\\Users\\benbi\\OneDrive\\שולחן העבודה\\files\\flash_card_files\\images\\right.png\\")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()