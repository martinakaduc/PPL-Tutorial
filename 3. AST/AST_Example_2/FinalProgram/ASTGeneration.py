from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils

            We need to visit all children of program. They are list of expressions.
            ctx.expression() returns the list we desire.

            Then we call expression.accept(self) or self.visitExpression(expression), 
            function visitExpression() will be triggered.
        '''
        expressions = [expression.accept(self) for expression in ctx.expression()]
        return Prog(expressions)

    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        '''
            BinOp: dataclass in ASTUtils
        '''
        if ctx.expression():
            return BinOp("+", ctx.expression().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx:BKITParser.TermContext):
        '''
            As defined in BKIT.g4, term can be either an Integer or an Id,
            so that we need to check if this term contains Integer or Id.

            Because Integer and Id are leaf nodes in AST, 
            we must directly call function self.visitInteger(ctx.Integer()) or self.visitId(ctx.Id())
        '''
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())
        elif ctx.Identifier():
            return self.visitIdentifier(ctx.Identifier())

    def visitInteger(self, node:BKITParser.Integer):
        '''
            Int: dataclass in ASTUtils
        '''
        return Int()

    def visitIdentifier(self, node:BKITParser.Identifier):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id()