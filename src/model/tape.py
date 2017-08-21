BLANK = '_'
LEFT = 'l'
RIGHT = 'r'
USED = '*'

class Tape(object):

    def __init__(self, head_position=1, cells=[]):
        self.head_position = head_position
        self.cells = cells

    def insert(self, input):
        self.cells.append(BLANK)
        self.cells += list(input.replace(' ', BLANK))
        self.cells.append(BLANK)

    def get_head_symbol(self):
        return self.cells[self.head_position]

    def get_head_position(self):
        return self.head_position

    def get_tape(self):
        return self.cells

    def move(self, direction):
        if direction == RIGHT:
            if self.head_position == len(self.cells)-1:
                self.cells.append(BLANK)
                self.head_position += 1
            else:
                self.head_position += 1

        elif direction == LEFT:
            if self.head_position == 0:
                self.cells = [BLANK] + self.cells
                self.head_position = 0
            else:
                self.head_position -= 1

    def write(self, symbol):
        if symbol != USED:
            self.cells[self.head_position] = symbol

    def __str__(self):
        return str(self.cells)

    def __repr__(self):
        return str(self.cells)