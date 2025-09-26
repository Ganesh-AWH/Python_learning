from tkinter import *
import pandas as pd
import random 

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    df = pd.read_csv(r"E:\Programming\Python\Udemy Course\Day31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"E:\Programming\Python\Udemy Course\Day31\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")
    

current_card = {}


def next_card():
    
    global current_card
    global flip_timer
    
    window.after_cancel(flip_timer)
    # window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
    
    

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image = back_image)
    
    
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(r"E:\Programming\Python\Udemy Course\Day31\data\words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#working with canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file=r"E:\Programming\Python\Udemy Course\Day31\images\card_front.png")
back_image = PhotoImage(file=r"E:\Programming\Python\Udemy Course\Day31\images\card_back.png")
canvas_background = canvas.create_image(400, 263,image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#buttons
cross_image = PhotoImage(file=r"E:\Programming\Python\Udemy Course\Day31\images\wrong.png")
unkonwn_buttons = Button(image=cross_image, highlightthickness=0, command=next_card)
unkonwn_buttons.grid(row=1, column=0)

check_image = PhotoImage(file=r"E:\Programming\Python\Udemy Course\Day31\images\right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


next_card()

window.mainloop()