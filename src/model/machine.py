from src.model.configuration import Configuration
from src.model.tape import Tape


class Machine:

    def __init__(self, tape=Tape(), configuration=Configuration()):
        self.tape = tape
        self.configuration = configuration


