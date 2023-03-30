
class Scoreboard:
    def __init__(self):
        self.guessed_states = []

    def score_guessed(self, a_state):
        self.guessed_states.append(a_state)

    def total_guessed(self):
        return self.guessed_states
