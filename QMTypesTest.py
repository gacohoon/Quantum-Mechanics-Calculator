"""Unit test of QMTypes.py"""

import unittest
from QMTypes import *
import classify

classifier = classify.Classifier(inputDict, outputDict)

class KnownTokens(unittest.TestCase):
    """Contains test string tokens, correctly identified classes and their
value"""
    knownTokens = (('1', Number, '1'),
                   ('-3', Number, '-3'),
                   ('-3.453234', Number, '-3.453234'),
                   ('.1', Number, '.1'),
                   ('-.7', Number, '-.7'),
                   ('3.1453e-10', Number, '3.1453e-10'),
                   ('-14E200', Number, '-14E200'),

                   ('A', Operator, 'A'),
                   ('b', Operator, 'b'),
                   ('z84zfex3', Operator, 'z84zfex3'),

                   ('+', Operation, '+'),
                   ('-', Operation, '-'),
                   ('*', Operation, '*'),
                   ('/', Operation, '/'),
                   ('^', Operation, '^'),
                   
                   ('<x|', Bra, 'x'),
                   ('<a01234|', Bra, 'a01234'),
                   ('<x7y5s7x920x4|', Bra, 'x7y5s7x920x4'),

                   ('|psi>', Ket, 'psi'),
                   ('|b56789>', Ket, 'b56789'),
                   ('|jf83nx0293xef>', Ket, 'jf83nx0293xef'))

    def testInputDictOnKnownTokens(self):
        """input dictionary should produce known classes from known tokens"""
        for token, Type, value in self.knownTokens:
            result = classifier.toClass(token)
            self.assertEqual(Type, result.__class__)

    def testOutputDictOnKnownClasses(self):
        """output dictionary should produce known tokens from known classes"""
        for token, Type, value in self.knownTokens:
            result = classifier.toToken(Type(value))
            self.assertEqual(token, result)

class BadTokens(unittest.TestCase):
    """Contains invalid Tokens"""
    badTokens = ('-1-', '-.a', '3a', '20x320x93E-10', '&', '$', '@', '<<a|',
                 '|a|', '<>', '1..')

    def testBadTokens(self):
        """bad tokens should raise ClassificationError"""
        for token in self.badTokens:
            self.assertRaises(classify.ClassificationError,
                              classifier.toClass, token)


if __name__ == '__main__':
    unittest.main()
