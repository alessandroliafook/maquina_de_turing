# noinspection PyUnresolvedReferences
from state import State

USED = '*'
COMMENTSYMBOL = ';'
BREAKLINE = '\n'

class Configuration:

    def __init__(self):
        self.states = {}

    def insert_state(self, state=State()):
        self.states[(state.name, state.symbol)] = state

    def upload_states_by_archive(self, path):
        arq = open(path)
        self.states.clear()
        for line in arq:
            if not line.startswith(COMMENTSYMBOL) and not line.startswith(BREAKLINE) and len(line) > 2:
                line = line.split(" ")
                line[-1] = line[-1].strip(BREAKLINE)
                state = State(line[0], line[1], line[2], line[3], line[4])
                self.insert_state(state)
        arq.close()

    def next_state(self, name, symbol):
        next_state = self.states.get((name, symbol))
        if next_state == None:
            next_state = self.states.get((name, USED))
        return next_state

    def __str__(self):
        return str(self.states.keys())

    def __repr__(self):
        return "Machine Configuration"