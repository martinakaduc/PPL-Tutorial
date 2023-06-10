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
        4,0,8,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,4,0,19,8,0,11,0,12,0,20,1,1,4,1,24,8,1,11,1,12,
        1,25,1,2,4,2,29,8,2,11,2,12,2,30,1,3,4,3,34,8,3,11,3,12,3,35,1,3,
        1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,1,0,4,1,0,48,57,1,0,97,122,1,0,63,63,3,0,9,10,13,13,
        32,32,50,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,18,1,0,0,0,3,23,1,0,
        0,0,5,28,1,0,0,0,7,33,1,0,0,0,9,39,1,0,0,0,11,41,1,0,0,0,13,43,1,
        0,0,0,15,45,1,0,0,0,17,19,7,0,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,
        18,1,0,0,0,20,21,1,0,0,0,21,2,1,0,0,0,22,24,7,1,0,0,23,22,1,0,0,
        0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,4,1,0,0,0,27,29,7,
        2,0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,
        6,1,0,0,0,32,34,7,3,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,
        0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,6,3,0,0,38,8,1,0,0,0,39,40,9,
        0,0,0,40,10,1,0,0,0,41,42,9,0,0,0,42,12,1,0,0,0,43,44,9,0,0,0,44,
        14,1,0,0,0,45,46,9,0,0,0,46,16,1,0,0,0,5,0,20,25,30,35,1,6,0,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ID = 2
    QUES = 3
    WS = 4
    ERROR_CHAR = 5
    UNCLOSE_STRING = 6
    ILLEGAL_ESCAPE = 7
    UNTERMINATED_COMMENT = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "QUES", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INT", "ID", "QUES", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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


