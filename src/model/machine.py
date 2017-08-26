import time

# noinspection PyUnresolvedReferences
from configuration import Configuration
# noinspection PyUnresolvedReferences
from tape import Tape

INITIALSTATENAME = '0'
ACCEPTANCESTATE = 'halt-accept'
BOUNCESTATE = 'halt-reject'

class Machine:

    def __init__(self, tape=Tape(), configuration=Configuration()):
        self.tape = tape
        self.configuration = configuration

    def upload_states_by_archive(self, path):
        self.configuration.upload_states_by_archive(path)

    def insert_tape(self, input):
        self.tape.insert(input)

    def run(self):
        current_state = self.configuration.next_state(INITIALSTATENAME, self.tape.get_head_symbol())
        while True:
            print ("Current state: " + str(current_state))
            print (self.tape)
            time.sleep(0.10)
            self.tape.write(current_state.new_symbol)
            self.tape.move(current_state.direction)

            if current_state.next_state_name in ACCEPTANCESTATE:
                print ("Accepted")
                break
            elif current_state.next_state_name in BOUNCESTATE:
                print ("Rejected")
                break

            state_aux = current_state
            current_state = self.configuration.next_state(state_aux.next_state_name, self.tape.get_head_symbol())
