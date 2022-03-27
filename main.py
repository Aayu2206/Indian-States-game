import turtle
import pandas

screen = turtle.Screen()

#Setting up screen
screen.title("Indian States Game")
image = "blank_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("29_states.csv")
states_list = data['state'].to_list()

# def get_coor(x,y):
#     '''gives the coordinates after clicking on screen'''
#     print(x,y)

# turtle.onscreenclick(get_coor)

correct_guesses_list = []
score = 0

while len(correct_guesses_list) < 29:

    answer_state = screen.textinput(title= f"{score}/29 States Correct",prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [ state for state in states_list if state not in correct_guesses_list]
        # missing_states = []
        # for state in states_list:
        #     if state not in correct_guesses_list:
        #         missing_states.append(state)

        #generates a file which contains missing states from the map 
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #Checks whether entered state is exact or not. 
    if answer_state in states_list:
        correct_guesses_list.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        # Fetching coordinates of state name
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        
turtle.mainloop()