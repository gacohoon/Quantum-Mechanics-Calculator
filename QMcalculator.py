"""Quantum mechanics calculator"""

import QMTypes
import classify


if __name__ == '__main__':
    c = classify.Classifier(QMTypes.inputDict, QMTypes.outputDict)
    ket = c.toClass('|a>')
    print c.toToken(ket)
