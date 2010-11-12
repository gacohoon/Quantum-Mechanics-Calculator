"""iostream.py - handles input and output
"""

import re
import QMTypes

# Define exceptions
class InputError(Exception):
    def __init__(self, string):
        self.msg = "Invalid input: {0}".format(string)
    def __str__(self):
        return repr(self.msg)


regexList = [r'[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?', # number
             r'<[a-zA-Z][a-zA-Z0-9]*[|]',  # Bra
             r'[|][a-zA-Z][a-zA-Z0-9]*>',  # Ket
             r'[a-zA-Z][a-zA-Z0-9]*',    # Operator
             '[+*/\-\^]']                  # Operation
             

def parse(s):
    """Parses string s into valid string tokens, eg Bra, Ket, number, etc."""
    s = s.replace('|', '||') # double each pipe in string
    tokenList = []
    for regex in regexList:
        tokenMatches = re.finditer(regex, s) # find all matches in string
        for eachMatch in tokenMatches:
            loc = eachMatch.span() # location of match: (begin, end)
            token = s[loc[0]:loc[1]] # string token
            tokenList.append([loc, token])
            s = s.replace(token, ' '*len(token), 1) # replace token with spaces

    # check to make sure all characters have been removed from s
    s = s.replace('|', ' ') # remove remaining pipes caused by single Bras/Kets
    if len(s.strip()) != 0:
        raise InputError(s.strip()) # display remaining characters in s

    tokenList.sort() # sort in place by location returned from span()
    tokens = [item[1] for item in tokenList] # add only string tokens, not loc
    return tokens

def assemble(tokenList):
    """Assembles valid tokens into an output string."""
    outputString = ''.join(tokenList) # combine tokens into string
    outputString = outputString.replace('||', '|') # remove double pipes
    return outputString


if __name__ == '__main__':
    test = '2.32432e * A 2+2 e2'
    t = ['<x|', 'H', '|x>']

    print parse(test)
