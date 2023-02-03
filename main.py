import turtle
import pandas as pd

my_screen = turtle.Screen()
my_screen.title("US States Game")
FONT = ('Arial', 10, 'bold')
# THIS IS HOW THE SCREEN BECOMES ANY GIF!!
my_image = "blank_states_img.gif"
my_screen.addshape(my_image)  # image is registered
turtle.shape(my_image)     # NOW image is visible (got turtleized??)
states_in_the_bag = []


# determine xy coordinates to build the state text locations:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# get the states master sheet:
data = pd.read_csv("50_states.csv")
mst_state = data.state.tolist()
#mst_state = mst_state.tolist()
guess_target = len(mst_state)
mst_x = data.x.tolist() #tolist can be applied to df or series
mst_y = data.y.tolist()
#i will be overiding the above to go w teacher's method below (based on answer state)

game_on = True
popup_title = "Guess the States"
#while game_on: #teacher's method is better -below
while len(states_in_the_bag) < len(mst_state):
    answer_state = my_screen.textinput(title=popup_title, prompt="Gimme a state").title()
    if answer_state == "Exit":
        break
    # is answer in state master
    if answer_state in mst_state:
        #answer_x = mst_x[mst_state.index(answer_state)]
        #teacher's method
        answer_row = data[data.state == answer_state]
        answer_x = int(answer_row.x)
        #answer_y = mst_y[mst_state.index(answer_state)]
        answer_y = int(answer_row.y)
        #IF GOOD GUESS: make a turtle, write to it, and post it
        good_guess = False
        if not answer_state in states_in_the_bag:
            states_in_the_bag.append(answer_state)
            good_guess = True
        if good_guess:
            t = turtle.Turtle()
            t.penup()
            t.goto((answer_x, answer_y))
            t.pendown()
            t.hideturtle()
            t.write(answer_state, font=FONT)
            #if not in the bag, put state in the bag!
            #format the score (displayed in popup_title)
            correct_guess_ctr = len(states_in_the_bag)
            popup_title = f"{correct_guess_ctr}/{guess_target} States Correct"
    else:
        pass
if answer_state == "Exit":
    #create a csv file w states to learn
    outfile = "states_to_learn.csv"   #contains just the names of states not guessed
    states_to_learn = []
    for state in mst_state:
        if not state in states_in_the_bag:
            states_to_learn.append(state)

    df_states_to_learn = pd.DataFrame(states_to_learn)
    df_states_to_learn.to_csv(outfile)

#finally, keep up the screen!
#turtle.mainloop()   #no longer needed cause now we type 'exit' to quit
#screen.exitonclick()  #superseeded above