class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class SyntaxError(Error):
    """
        Exception raised for errors in the syntax of the turing machine

        Attributes:
            menssage -- explanation of the error
            line -- line that error accur
            expression -- input expression in with error occurred
    """
    def __init__(self, message, line):
        self.line = line
        self.message = message
        self.expression = "At line %d. %s" % (self.line + 1, self.message)
