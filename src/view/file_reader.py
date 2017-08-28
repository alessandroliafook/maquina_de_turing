from src.model.state import State

COMMENTSYMBOL = ';'
BREAKLINE = '\n'

def file_reader(path):
    arq = open(path)
    states = {}
    for line in arq:
        if not line.startswith(COMMENTSYMBOL) and not line.startswith(BREAKLINE) and len(line) > 2:
            line = line.split(" ")
            line[-1] = line[-1].strip(BREAKLINE)
            state = State(line[0], line[1], line[2], line[3], line[4])
            states[(state.name, state.symbol)] = state

    arq.close()
    return states