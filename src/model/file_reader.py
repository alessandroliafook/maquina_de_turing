from state import State

COMMENTSYMBOL = ';'

'''
    Filters the file according to: <current state> <current symbol> <new symbol> <direction> <new state>
    Returns a dictionary in the format described above.
'''
def file_reader(path):

    try:
        arq = open(path)
    except IOError:
        return

    states = {}

    for line in arq:
        if not line.startswith(COMMENTSYMBOL) and not line.startswith("\n") and len(line) > 2:
            line = line.split(" ")
            line[-1] = line[-1].strip("\n")
            state = State(line[0], line[1], line[2], line[3], line[4])
            states[(state.name, state.symbol)] = state

    arq.close()
    return states
