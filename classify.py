"""Module used to convert between QMType classes and string tokens"""

import re
from QMTypes import Expression

# Define exceptions
class ClassificationError(Exception):
    def __init__(self, string):
        self.msg = "Cannot classify {0} from provided dictionary".format(string)
    def __str__(self):
        return repr(self.msg)

class Classifier(object):
    """Class which will matches tokens to their appropriate objects."""
    def __init__(self, inputDict, outputDict):
        """inputDict is a dictionary containing regular expression strings
and their associated classes to instantiate.

inputDict = {regex0: class0,
             regex1: class1,
             regex2: class3}

outputDict is a dictionary containing classes and their associated string tokens

outputDict = {class0: string0,
              class1: string1,
              class2: string2}
"""
        self.inputDict = inputDict
        self.outputDict = outputDict

    def toClass(self, stringToClassify):
        """Attempt to match string token to an object in the dictionary."""
        for regex, Type in self.inputDict.iteritems():
            match =  re.search(regex, stringToClassify)
            if match is not None:
                return Type(match.groups()[0]) # first element in tuple
            else:
                pass
        raise ClassificationError(stringToClassify) # no match in dictionary

    def toToken(self, classToTokenize):
        """Attempt to create string token from classes in dictionary. Also
replaces 'val' with actual class.val value."""
        try:
            token = self.outputDict[classToTokenize.__class__] # lookup class
            return token.replace('val', classToTokenize.val)
        except KeyError:
            raise ClassificationError(classToTokenize)

    def toExpr(self, inputTokenList):
        """Converts a list of string tokens into an expression"""
        classList = []
        for token in inputTokenList:
            qmClass = c.toClass(token)
            classList.append(qmClass)
        return Expression(classList)

    def toTokenList(self, expression):
        """Converts an expression into a token list"""
        tokenList = []
        for qmClass in expression.contents:
            token = c.toToken(qmClass)
            tokenList.append(token)
        return tokenList
