# noinspection PyUnresolvedReferences
from state import State

USED = '*'
COMMENTSYMBOL = ';'

class Machine_Program:
    """
        The class Configuration contains a state dictionary for Turing Machine
        Syntax: '<current state> <current symbol> <new symbol> <direction> <new state>'.
        The key to the dictionary is a tuple: (state name, current symbol)
    """
    def __init__(self):
        self.states = {}

    def have_states(self):
        return bool(self.states)

    def insert_state(self, state=State()):
        self.states[(state.name, state.symbol)] = state

    def set_states(self, states):
        self.states.clear()
        self.states = states

    def next_state(self, name, symbol):
        next_state = self.states.get((name, symbol))
        if next_state is None:
            next_state = self.states.get((name, USED))
        return next_state

    def __str__(self):
        return str(self.states.keys())

    def __repr__(self):
        return "Machine Program"
