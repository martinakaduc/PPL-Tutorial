# Generated from BKIT.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,10,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,4,4,31,8,4,11,4,12,4,32,1,5,4,5,36,8,5,11,5,12,5,37,1,5,1,5,1,
        6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,50,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,
        0,3,23,1,0,0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,30,1,0,0,0,11,35,1,0,
        0,0,13,41,1,0,0,0,15,43,1,0,0,0,17,45,1,0,0,0,19,47,1,0,0,0,21,22,
        5,43,0,0,22,2,1,0,0,0,23,24,5,45,0,0,24,4,1,0,0,0,25,26,5,42,0,0,
        26,6,1,0,0,0,27,28,5,47,0,0,28,8,1,0,0,0,29,31,7,0,0,0,30,29,1,0,
        0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,10,1,0,0,0,34,36,
        7,1,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,
        38,39,1,0,0,0,39,40,6,5,0,0,40,12,1,0,0,0,41,42,9,0,0,0,42,14,1,
        0,0,0,43,44,9,0,0,0,44,16,1,0,0,0,45,46,9,0,0,0,46,18,1,0,0,0,47,
        48,9,0,0,0,48,20,1,0,0,0,3,0,32,37,1,6,0,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Add = 1
    Sub = 2
    Mul = 3
    Div = 4
    Integer = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9
    UNTERMINATED_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "Add", "Sub", "Mul", "Div", "Integer", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Add", "Sub", "Mul", "Div", "Integer", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


