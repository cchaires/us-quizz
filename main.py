"""# get the coordinates clicking the map
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)"""
import turtle
from states_list import State
from scoreboard import  Scoreboard


screen = turtle.Screen()
screen.title("Quizz U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = Scoreboard()
states = State(score)

while len(score.total_guessed()) < 50:
    answer_state = screen.textinput(f"{len(score.total_guessed())}/50 Guess the State",
                                    "Whats another state's name? ").title()
    if answer_state == "Exit":
        break
    elif states.check_if_exists(answer_state):
        score.score_guessed(answer_state)
        states.print_state(answer_state)

states.not_in_the_list()
states.create_difference()
