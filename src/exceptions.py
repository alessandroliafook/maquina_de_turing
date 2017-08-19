from src import SyntaxError
from src import Error


class CommandDirectionError(SyntaxError):
    """
        Exception raised for errors in the direction of the command.
    """

    def __init__(self, line):
        super("The direction of the command doesn't match the pattern 'l', 'r' \
or '*'.", line)


class CommandStateError(SyntaxError):
    """
        Exception raised for errors in the state command.
    """

    def __init__(self, line):
        super("The state of the command doesn't match the pattern \
'q<digit,a,r>'.")


class InputProcessError(Error):
    """
        Exception raised for errors in the state command.

        Attributes:
            expression -- input expression in with error occurred
    """

    def __init__(self, state, input):
        self.expression = "The state " + state + " cannot process the " + input + " character\
, please check your commands and try again."


class StateNotFoundError(Error):
    """
        Exception raised for errors in find a valid state.
        
        Attributes:
            expression -- input expression in with error occurred
    """

    def __init__(self, state):
        self.expression = "Your commands doesn't have a " + string + " state"


class TransitionError(SyntaxError):
    """
        Exception raised for errors of duplicated line.
    """

    def __init__(self, state, line):
        super("Your commands have a duplicated line, please fix the problem \
and rerun the application. State: " + state, line)
