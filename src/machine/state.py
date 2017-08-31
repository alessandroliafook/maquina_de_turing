

'''
    Simulates a state with the following syntax:
    '<current state> <current symbol> <new symbol> <direction> <new state>'
'''

class State(object):

    def __init__(self, name='', symbol='', new_symbol='', direction='', next_state_name=''):
        self.name = name
        self.symbol = symbol
        self.new_symbol = new_symbol
        self.direction = direction
        self.next_state_name = next_state_name

    def __str__(self):
        return 'State %s' % self.name

    def __repr__(self):
        return '%s %s %s %s %s' %(self.name, self.symbol, self.new_symbol, self.direction, self.next_state_name)

    def update_state(self, name='', symbol='', new_symbol='', direction='', next_state_name=''):
        self.name = name
        self.symbol = symbol
        self.new_symbol = new_symbol
        self.direction = direction
        self.next_state_name = next_state_name
