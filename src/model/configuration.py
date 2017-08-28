# noinspection PyUnresolvedReferences
from state import State

from src.view.file_reader import file_reader

USED = '*'
COMMENTSYMBOL = ';'
BREAKLINE = '\n'


class Configuration:

    def __init__(self):
        self.states = {}

    def insert_state(self, state=State()):
        self.states[(state.name, state.symbol)] = state

    def upload_states_by_archive(self, path):
        states = file_reader(path)
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
        return "Machine Configuration"
