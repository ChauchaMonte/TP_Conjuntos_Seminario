# Generated from Aritmetica.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AritmeticaParser import AritmeticaParser
else:
    from AritmeticaParser import AritmeticaParser

# This class defines a complete listener for a parse tree produced by AritmeticaParser.
class AritmeticaListener(ParseTreeListener):

    # Enter a parse tree produced by AritmeticaParser#program.
    def enterProgram(self, ctx:AritmeticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#program.
    def exitProgram(self, ctx:AritmeticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#statement.
    def enterStatement(self, ctx:AritmeticaParser.StatementContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#statement.
    def exitStatement(self, ctx:AritmeticaParser.StatementContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setMathematicsManager.
    def enterSetMathematicsManager(self, ctx:AritmeticaParser.SetMathematicsManagerContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setMathematicsManager.
    def exitSetMathematicsManager(self, ctx:AritmeticaParser.SetMathematicsManagerContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#getIntersection.
    def enterGetIntersection(self, ctx:AritmeticaParser.GetIntersectionContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#getIntersection.
    def exitGetIntersection(self, ctx:AritmeticaParser.GetIntersectionContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setNumber.
    def enterSetNumber(self, ctx:AritmeticaParser.SetNumberContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setNumber.
    def exitSetNumber(self, ctx:AritmeticaParser.SetNumberContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setMerge.
    def enterSetMerge(self, ctx:AritmeticaParser.SetMergeContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setMerge.
    def exitSetMerge(self, ctx:AritmeticaParser.SetMergeContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setDifference.
    def enterSetDifference(self, ctx:AritmeticaParser.SetDifferenceContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setDifference.
    def exitSetDifference(self, ctx:AritmeticaParser.SetDifferenceContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setComplement.
    def enterSetComplement(self, ctx:AritmeticaParser.SetComplementContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setComplement.
    def exitSetComplement(self, ctx:AritmeticaParser.SetComplementContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setBelongs.
    def enterSetBelongs(self, ctx:AritmeticaParser.SetBelongsContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setBelongs.
    def exitSetBelongs(self, ctx:AritmeticaParser.SetBelongsContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setSum.
    def enterSetSum(self, ctx:AritmeticaParser.SetSumContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setSum.
    def exitSetSum(self, ctx:AritmeticaParser.SetSumContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setAverage.
    def enterSetAverage(self, ctx:AritmeticaParser.SetAverageContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setAverage.
    def exitSetAverage(self, ctx:AritmeticaParser.SetAverageContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setLength.
    def enterSetLength(self, ctx:AritmeticaParser.SetLengthContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setLength.
    def exitSetLength(self, ctx:AritmeticaParser.SetLengthContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#setPrint.
    def enterSetPrint(self, ctx:AritmeticaParser.SetPrintContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#setPrint.
    def exitSetPrint(self, ctx:AritmeticaParser.SetPrintContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#assignStatement.
    def enterAssignStatement(self, ctx:AritmeticaParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#assignStatement.
    def exitAssignStatement(self, ctx:AritmeticaParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#ifStatement.
    def enterIfStatement(self, ctx:AritmeticaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#ifStatement.
    def exitIfStatement(self, ctx:AritmeticaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#whileStatement.
    def enterWhileStatement(self, ctx:AritmeticaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#whileStatement.
    def exitWhileStatement(self, ctx:AritmeticaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#booleanExpression.
    def enterBooleanExpression(self, ctx:AritmeticaParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#booleanExpression.
    def exitBooleanExpression(self, ctx:AritmeticaParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#operand.
    def enterOperand(self, ctx:AritmeticaParser.OperandContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#operand.
    def exitOperand(self, ctx:AritmeticaParser.OperandContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#expression.
    def enterExpression(self, ctx:AritmeticaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#expression.
    def exitExpression(self, ctx:AritmeticaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#term.
    def enterTerm(self, ctx:AritmeticaParser.TermContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#term.
    def exitTerm(self, ctx:AritmeticaParser.TermContext):
        pass


    # Enter a parse tree produced by AritmeticaParser#factor.
    def enterFactor(self, ctx:AritmeticaParser.FactorContext):
        pass

    # Exit a parse tree produced by AritmeticaParser#factor.
    def exitFactor(self, ctx:AritmeticaParser.FactorContext):
        pass


