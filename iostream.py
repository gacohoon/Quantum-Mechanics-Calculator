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


regexList = ['(<[a-zA-Z][a-zA-Z0-9]*[|])', # Bra
             '([|][a-zA-Z][a-zA-Z0-9]*>)'] # Ket

def parse(s):
    """Parses string s into valid string tokens, eg Bra, Ket, number, etc."""
    tokenList = []
    for regex in regexList:
        tokenMatches = re.finditer(regex, s) # find all matches in string
        for eachMatch in tokenMatches:
            loc = eachMatch.span() # location of match: (begin, end)
            token = s[loc[0]:loc[1]] # string token
            tokenList.append([loc, token])

    tokenList.sort() # sort in place by location returned from span()
    tokens = [item[1] for item in tokenList] # add only string tokens, not loc
    return tokens

def assemble(tokenList):
    """Assembles valid tokens into an output string."""
    outputString = ''.join(tokenList) # combine tokens into string
    outputString = outputString.replace('||', '|') # remove double pipes
    return outputString


if __name__ == '__main__':
    test = '<a|b><c|d>'
    t = ['<a|', '|b>', '<c|', '|d>']

    print parse(test)
