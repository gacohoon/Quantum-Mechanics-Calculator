"""Unit test for iostream.py"""

import unittest
import iostream

class KnownStrings(unittest.TestCase):
    """Contains test strings and a list of correctly separated tokens"""
    knownStrings = (('<a|', ['<a|']),
                   ('|a>', ['|a>']),
                   ('<a|b>', ['<a|', '|b>']),
                   ('|a><b|', ['|a>', '<b|']),
                   ('<a|b><c|d>', ['<a|', '|b>', '<c|', '|d>']),
                   ('<a|b|a>', ['<a|', 'b', '|a>']),
                   ('2+3', ['2', '+', '3']),
                   ('1-7', ['1', '-', '7']),
                   ('2*4', ['2', '*', '4']),
                   ('11/10', ['11', '/', '10']),
                   ('6^4', ['6', '^', '4']),
                   ('2*2', ['2', '*', '2']),
                   ('2.34*A', ['2.34', '*', 'A']),
                   ('2.3e-10', ['2.3e-10']),
                   ('-2', ['-', '2']))

    def testParseKnownStrings(self):
        """parse should separate known strings into known tokens"""
        for expression, terms in self.knownStrings:
            result = iostream.parse(expression)
            self.assertEqual(terms, result)

    def testAssembleKnownStrings(self):
        """assemble should combine known tokens into known strings"""
        for expression, terms in self.knownStrings:
            result = iostream.assemble(terms)
            self.assertEqual(result, expression)

class BadStrings(unittest.TestCase):
    """Contains invalid input strings"""
    badStrings = ('&', '$', '@', '<<a|', '<>', '1..')

    def testBadStrings(self):
        """bad strings should raise InputError"""
        for string in self.badStrings:
            self.assertRaises(iostream.InputError, iostream.parse, string)

if __name__ == '__main__':
    unittest.main()
