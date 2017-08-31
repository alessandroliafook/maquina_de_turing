# coding: utf-8

from machine_program import Machine_Program
from file_reader import file_reader
from tape import Tape

INITIALSTATENAME = '0'
ACCEPTANCESTATE = 'halt-accept'
BOUNCESTATE = 'halt-reject'


class Machine:

    def __init__(self, tape=Tape(), machine_program=Machine_Program()):
        self.tape = tape #object tape
        self.machine_program = machine_program #object Machine_program

    def have_program(self):
        return self.machine_program.have_states()

    def load_program(self, path):
        states = file_reader(path)
        self.machine_program.set_states(states)

    def insert_tape(self, input):
        self.tape.insert(input)

    def run(self):
        # read initial state
        steps = 0
        current_state = self.machine_program.next_state(INITIALSTATENAME, self.tape.get_head_symbol())
        while True:
            #time.sleep(0.3)
            if current_state is not None:
                self.print_current_configuration(self.tape, current_state.name, steps)
                self.print_tape(self.tape)
                steps += 1
                # write
                self.tape.write(current_state.new_symbol)
                # move
                self.tape.move(current_state.direction)
                # Verify halt status
                if self.verify_halt(current_state.next_state_name, self.tape, steps):
                    break
                # read next state
                state_aux = current_state
                current_state = self.machine_program.next_state(state_aux.next_state_name, self.tape.get_head_symbol())
            else:
                print("========= Halted =========")
                break

    def verify_halt(self, next_state_name, tape, steps):
        # verifies acceptance states
        if next_state_name == ACCEPTANCESTATE or next_state_name == BOUNCESTATE:
            self.print_current_configuration(self.tape, next_state_name, steps)
            self.print_tape(self.tape)
            print("========= Halted =========")
            return True
        elif next_state_name == "halt":
            self.print_current_configuration(self.tape, next_state_name, steps)
            self.print_tape(self.tape)
            print("========= Halted =========")
            return True
        else:
            return False

    def print_tape(self, tape):
        print("Tape: \n" + tape.get_head_pointer())
        print(tape)

    def print_current_configuration(self, tape, current_state_name, steps):
        print("Current state: %s | Head Position: %d | Steps: %d" % (current_state_name, tape.get_head_position(), steps))
