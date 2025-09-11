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

total_count = len(us_df)
guess_count = 0


while guess_count < 2:

    #taking the state from user
    answer = screen.textinput(title=f"{guess_count}/{total_count} correct", prompt="what's another state's name?").title()
    #capitalizing the text
    # capitalized_state = answer_state.capitalize()

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
        guess_count += 1

screen.exitonclick()
