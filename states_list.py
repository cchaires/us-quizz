import pandas
from turtle import Turtle

# reading the csv file
data = pandas.read_csv("50_states.csv")
# splitting into states
states_list = data["state"].to_list()
# Constants
ALIGNMENT = "center"
FONT = ("Consolas", 10, "bold")


class State:
    def __init__(self, guessed_by_user):
        self.t = Turtle()
        self.t.penup()
        self.t.hideturtle()
        self.t.color("black")
        self.states_list = data["state"].to_list()
        self.not_guessed_by_user = []
        self.guessed_by_user = guessed_by_user

    def check_if_exists(self, a_state):
        if a_state in self.states_list:
            return True

    def print_state(self, a_state):
        states_data = data[data.state == a_state]
        self.t.goto(int(states_data.x), int(states_data.y))
        self.t.write(f"{states_data.state.item()}", align=ALIGNMENT, font=FONT)

    def not_in_the_list(self):
        difference = list(filter(lambda state: state not in self.guessed_by_user.total_guessed(), self.states_list))
        self.not_guessed_by_user.extend(difference)

    def create_difference(self):
        df = pandas.DataFrame(self.not_guessed_by_user)
        df.to_csv("difference.csv")
        print(f"File saved: {len(self.not_guessed_by_user)} differences.")

