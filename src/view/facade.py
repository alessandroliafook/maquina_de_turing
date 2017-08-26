from src.controller.manager import Manager

OPTIONS = "\nPress 'I' to import a program, or 'C' to close the simulator: "

class Facade:
    def __init__(self):
        self.manager = Manager()

    def start(self):
        self.print_header()
        while True:
            option = raw_input(OPTIONS)
            if option.lower() == 'i':
                path = self.get_program_path()
                tape = self.get_input_word()
                self.manager.mount_machine(path, tape)

            elif option.lower() == 'c':
                print "Closing simulator..."
                break
            else:
                print "Invalid option"  # to do: exception



    def print_header(self):
        print "=== Welcome to Turing Machine Simulator ==="
        print "> Syntax: "
        print "  Each line of the file must follow this pattern (separated by spaces):"
        print "    <current state> <current symbol> <new symbol> <direction> <new state>"
        print "  You can use any number or word for <current state> and <new state>, eg. 10, a, state1" \
              " (state labels are case-sensitive)."
        print "  You can use any character for <current symbol> and <new symbol>, or '_' to represent blank (space)" \
              " (symbols are case-sensitve)."
        print "  <direction> should be 'l', 'r' or '*', denoting 'move left', 'move right' or 'do not move'," \
              " respectively."
        print "  Anything after a ';' is a comment."
        print "  The machine halts when it reaches any state starting with 'halt', eg. halt, halt-accept."

    def get_program_path(self):
        print "> Write the path of the file containing the commands and press 'Enter':"
        path = raw_input()
        return path

    def get_input_word(self):
        print "> Write the input word:"
        word = raw_input()
        return word


