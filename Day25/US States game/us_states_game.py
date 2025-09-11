from array import array
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("Us state game")
# image link
image = r"Day25\US States game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#taking total count of states
us_df = pd.read_csv(r"Day25\US States game\50_states.csv")
all_states = us_df.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    #taking the state from user
    answer = screen.textinput(title=f"{len(guessed_states)}/ 50 correct", prompt="what's another state's name?").title()
    
    if answer == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        
        #taking the missing values list to new csv file  "states to learn.csv"
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv(r"Day25\US States game\states to learn.csv")
        break
        
    if answer in all_states:
        #create the turtle class to writ in map
        tut = turtle.Turtle()
        tut.hideturtle()
        tut.penup()
        
        #taking that row
        answer_state = us_df[us_df["state"] == answer]
        x_cor = answer_state.x.item()
        y_cor = answer_state.y.item()
        
        tut.goto(x_cor, y_cor)
        tut.write(f"{answer}", font = ("Arial", 8, "normal"))
        guessed_states.append(answer)


