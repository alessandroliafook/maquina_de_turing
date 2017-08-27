# coding: utf-8

import time

# noinspection PyUnresolvedReferences
from configuration import Configuration
# noinspection PyUnresolvedReferences
from tape import Tape

INITIALSTATENAME = '0'
ACCEPTANCESTATE = 'halt-accept'
BOUNCESTATE = 'halt-reject'
BREAKLINE = '\n'


class Machine:

    def __init__(self, tape=Tape(), configuration=Configuration()):
        self.tape = tape
        self.configuration = configuration
        self.steps = []

    def upload_states_by_archive(self, path):
        self.configuration.upload_states_by_archive(path)

    def insert_tape(self, input):
        self.tape.insert(input)

    def run(self):
        cont = 0
        current_state = self.configuration.next_state(INITIALSTATENAME, self.tape.get_head_symbol())
        while True:
            time.sleep(0.10)
            print ("Current state: %s | Head Position: %d | Steps: %d" % (str(current_state),
                                                                          self.tape.get_head_position(), cont))
            print ("Tape: " + BREAKLINE + self.tape.get_head_pointer())
            print (self.tape)
            if current_state is not None:
                self.tape.write(current_state.new_symbol)
                self.tape.move(current_state.direction)
                cont += 1
                step = (current_state.name, cont, self.tape.get_head_pointer(), str(self.tape))
                self.steps.append(step)
                if current_state.next_state_name in ACCEPTANCESTATE:
                    print ("Current state: %s | Head Position: %d | Steps: %d" % (str(current_state),
                                                                                  self.tape.get_head_position(), cont))
                    print ("=== Accepted ===")
                    break
                elif current_state.next_state_name in BOUNCESTATE:
                    print ("Current state: %s | Head Position: %d | Steps: %d" % (str(current_state),
                                                                                  self.tape.get_head_position(), cont))
                    print ("=== Rejected ===")
                    break

                state_aux = current_state
                current_state = self.configuration.next_state(state_aux.next_state_name, self.tape.get_head_symbol())
            else:
                break

    def run_steps(self):
        command = raw_input("press n to next step or r to run: ")
        for step in self.steps:
            if command.lower() == "n":
                self.print_step(step)
                command = raw_input("press n to next step or r to run: ")
            elif command.lower() == "r":
                self.print_step(step)
            else:
                print "opcao invalida, vai ate o fim msm"
                self.print_step(step)

    def print_step(self, step):
        print ("Current state: %s | Steps: %d" % (step[0], step[1]))
        print ("Tape: " + BREAKLINE + step[2])
        print (step[3])
