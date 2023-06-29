from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *
from functools import reduce

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return Prog([ctx.expression().accept(self)])

    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if ctx.expression():
            sign = ""
            if ctx.Add():
                sign = "+"
            elif ctx.Sub():
                sign = "-"
            
            return BinOp(sign, ctx.expression().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx:BKITParser.TermContext):
        if ctx.term():
            sign = ""
            if ctx.Mul():
                sign = "*"
            elif ctx.Div():
                sign = "/"
            
            return BinOp(sign, ctx.term().accept(self), ctx.factor().accept(self))
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx:BKITParser.FactorContext):
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())

    def visitInteger(self, node:BKITParser.Integer):
        return Int(int(node.getText()))