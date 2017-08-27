from src.model.machine import Machine


class Manager:
    def __init__(self):
        self.machine = Machine()

    def mount_machine(self, path, tape):
        self.machine.upload_states_by_archive(path)
        self.machine.insert_tape(tape)
        self.start_machine()

    def start_machine(self):
        print self.machine.run()
