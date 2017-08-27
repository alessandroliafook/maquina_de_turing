# coding: utf-8

BLANK = '_'
LEFT = 'l'
RIGHT = 'r'
USED = '*'


class Tape(object):

    def __init__(self, head_position=1, cells=[]):
        self.head_position = head_position
        self.cells = cells

    def insert(self, input):
        self.cells = [] #clear cells
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
        tape = " ".join(self.cells).replace("_", " ")
        return tape

    def get_head_pointer(self):
        head_pointer = ""
        for i in range(len(self.cells)):
            if i == self.head_position:
                head_pointer += "↓ "
            else:
                head_pointer += "  "
        return head_pointer

    def __repr__(self):
        return str(self.cells)
