from src.view import data_validator


class State(object):

    def __init__(self, name):

        self.name = name
        self.functions = {}

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return str(self.name)

    def add_transition(self, input_symbol, write_symbol, direction_symbol,
                       next_state):

        transition = [write_symbol, direction_symbol, next_state]
        data_validator.transition(self, input_symbol, direction_symbol, 
                                  next_state)

        self.functions[input_symbol] = transition

    def process(self, input):

        data_validator.input(self, input)

        return self.functions[input][:]
