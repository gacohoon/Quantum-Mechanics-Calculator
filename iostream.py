"""Module used to for string and determine if it is a valid
expression of dirac notation in quantum mechanics."""

# Define exceptions
class InputError(Exception):
    def __init__(self, string):
        self.msg = "Invalid input: {0}".format(string)
    def __str__(self):
        return repr(self.msg)

def parse(s):
    """Parses string s into valid string tokens, eg Bra, Ket, number, etc."""
    pass

def assemble(tokenList):
    """Assembles valid tokens into an output string."""
    pass
