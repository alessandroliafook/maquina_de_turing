BLANK = '_'
LEFT = 'l'
RIGHT = 'r'
USED = '*'


class Tape(object):

    def __init__(self):

        self.position = 1
        self.input = []

    def insert(self, input):
        self.input.append(BLANK)

        if input == '':
            self.input.append(BLANK)
            return

        for i in xrange(len(input)):
            self.input.append(input[i])

        self.input.append(BLANK)

    def get_symbol(self):
        return self.input[self.position]

    def get_position(self):
        return str(self.position)

    def move(self, direction):

        if direction == LEFT:
            self.position -= 1

        else if direction == RIGHT:
            self.position += 1

        else if direction == USED:
            # to be sure that is do nothing in this case
            return

    def write(self, symbol):
        if symbol != USED:
            self.input.[self.position] = symbol

    def get_tape(self):
        return str(self.input)
