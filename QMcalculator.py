"""Quantum mechanics calculator

Run using:

python QMcalculator.py


"""

import QMTypes
import classify
import iostream

class CommandLinePrompt(object):
    """Current interface to the quantum mechanics calculator."""
    def __init__(self, program):
        self.history = []
        self.main = program

    def run(self):
        """Begin the command line program"""
        print """
#    Quantum Mechanics Calculator 
#
#    Copyright (C) 2010  Jeffrey M. Brown, Kyle T. Taylor
#
#    Type 'exit' to quit.
     
"""
        while 1:
            line = raw_input('> ') # get a line from the prompt
            self.history.append(line) # keep track of commands
            if line == 'exit': break

            try:
                self.main(line)
            except iostream.InputError, classify.ClassificationError:
                print "Invalid input"

def main(line):
    c = classify.Classifier(QMTypes.inputDict, QMTypes.outputDict)
    
    inputTokenList = iostream.parse(line) # parse input
    classList = []
    for token in inputTokenList:
        qmClass = c.toClass(token) # convert input into classes
        classList.append(qmClass)
    print classList # display all classes that were identified

    outputTokenList = []
    for qmClass in classList:
        token = c.toToken(qmClass) # create token for each class
        outputTokenList.append(token)
    outputString = iostream.assemble(outputTokenList)
    print outputString, '\n'

            

if __name__ == '__main__':
    CLP = CommandLinePrompt(main)
    CLP.run()
