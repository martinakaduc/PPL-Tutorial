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
        4,0,8,44,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,4,1,21,8,1,11,1,12,1,22,1,2,4,2,26,8,2,
        11,2,12,2,27,1,3,4,3,31,8,3,11,3,12,3,32,1,3,1,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,3,1,
        0,48,57,1,0,97,122,3,0,9,10,13,13,32,32,46,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,1,17,1,0,0,0,3,20,1,0,0,0,5,25,1,0,0,0,7,30,1,0,0,0,
        9,36,1,0,0,0,11,38,1,0,0,0,13,40,1,0,0,0,15,42,1,0,0,0,17,18,5,43,
        0,0,18,2,1,0,0,0,19,21,7,0,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,
        1,0,0,0,22,23,1,0,0,0,23,4,1,0,0,0,24,26,7,1,0,0,25,24,1,0,0,0,26,
        27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,6,1,0,0,0,29,31,7,2,0,
        0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,34,
        1,0,0,0,34,35,6,3,0,0,35,8,1,0,0,0,36,37,9,0,0,0,37,10,1,0,0,0,38,
        39,9,0,0,0,39,12,1,0,0,0,40,41,9,0,0,0,41,14,1,0,0,0,42,43,9,0,0,
        0,43,16,1,0,0,0,4,0,22,27,32,1,6,0,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Integer = 2
    Identifier = 3
    WS = 4
    ERROR_CHAR = 5
    UNCLOSE_STRING = 6
    ILLEGAL_ESCAPE = 7
    UNTERMINATED_COMMENT = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'" ]

    symbolicNames = [ "<INVALID>",
            "Integer", "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "Integer", "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


