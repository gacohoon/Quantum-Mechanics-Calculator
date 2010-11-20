"""Module containing quantum mechanical classes"""

class QMType(object):
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return (type(self)==type(other)) and (self.val == other.val)

class Number(QMType):
    """Wrapper class for numerical values"""
    def __init__(self, value):
        QMType.__init__(self, value)

class Operation(QMType):
    """Class for basic mathematical operations, e.g. +, -, *, /"""
    def __init__(self, operation):
        QMType.__init__(self, operation)

class Operator(QMType):
    """Class for representing operators"""
    def __init__(self, name):
        QMType.__init__(self, name)

class Bra(QMType):
    """Class for representing a bra in Dirac notation: <a|"""
    def __init__(self, name):
        QMType.__init__(self, name)

class Ket(QMType):
    """Class for representing a ket in Dirac notation: |a>"""
    def __init__(self, name):
        QMType.__init__(self, name)

class State(QMType):
    """Class for representing bras and kets in Dirac notation: <a| or |a>"""
    def __init__(self, stateType, name):
        QMType.__init__(self, name)
        self.stateType = stateType  #Bra or Ket
    def __repr__(self):
        retVal = ""
        if self.stateType == "bra":
            retVal += "<" + str(self.Val) + "|"
        else:
            retVal += "|" + str(self.Val) + ">"
        return retVal

# Dictionary containing regular expressions of quantum mechanical string tokens
# and their associated classes
inputDict = {r'^([+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)$': Number,
             '^([+*/\-]|[\^])$': Operation,
             '^([a-zA-Z][a-zA-Z0-9]*)$': Operator,
             '^<([a-zA-Z][a-zA-Z0-9]*)[|]$': Bra,
             '^[|]([a-zA-Z][a-zA-Z0-9]*)>$': Ket}

# Dictionary containing QM classes and their associated strings tokens
outputDict = {Number: 'val',
              Operation: 'val',
              Operator: 'val',
              Bra: '<val|',
              Ket: '|val>'}
