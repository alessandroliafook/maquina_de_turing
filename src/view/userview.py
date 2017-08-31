from controller.manager import Manager
from view import data_validator
import time

OPTIONS = "\n" + "="*61 + "\nPress 'I' to import a program, or 'C' to close the simulator: "


class UserView:

    def __init__(self):
        self.manager = Manager()

    def start(self):
        self.print_header()
        while True:
            option = raw_input(OPTIONS)

            if option.lower() == 'i':
                path = self.get_program_path()
                if data_validator.validade_path(path):
                    tape = self.get_input_word()
                    self.manager.mount_machine(path, tape)
                else:
                    print ("Wrong program path!!!")

            elif option.lower() == 'c':
                print ("Closing simulator...")
                time.sleep(0.5)
                break
            else:
                print ("Invalid option")  # to do: exception

    def print_header(self):
        header = "=== Welcome to Turing Machine Simulator ===\n" \
                 "> Syntax: \n" \
                 "\tEach line of the file must follow this pattern (separated by spaces): <current state> <current symbol> <new symbol> <direction> <new state>\n" \
                 "\tYou can use any number or word for <current state> and <new state>, eg. 10, a, state1  (state labels are case-sensitive).\n" \
                 "\tYou can use any character for <current symbol> and <new symbol>, or '_' to represent blank (space)  (symbols are case-sensitve).\n" \
                 "\t<direction> should be 'l', 'r' or '*', denoting 'move left', 'move right' or 'do not move', respectively.\n" \
                 "\tAnything after a ';' is a comment.\n" \
                 "\tThe machine halts when it reaches any state starting with 'halt', eg. halt, halt-accept."
        print header

    def get_program_path(self):
        print ("> Write the path of the file containing the commands and press 'Enter':")
        path = raw_input()
        return path

    def get_input_word(self):
        print ("> Write the input word:")
        word = raw_input()
        return word

