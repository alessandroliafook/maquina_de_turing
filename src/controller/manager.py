from src.model.machine import Machine


class Manager:

    def __init__(self):
        self.machine = Machine()

    def mount_machine(self, path, tape):
        self.machine.load_states_from_file(path)
        self.machine.insert_tape(tape)
        return self.start_machine()

    def start_machine(self):
        if self.machine.have_configuration():
            self.machine.run()
            return True
        else:
            return False
