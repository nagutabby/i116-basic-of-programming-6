from parse_tree import ExpressionParseTree, NumberParseTree, AdditionParseTree, MultiplicationParseTree, RemainderParseTree
from custom_exception import DivisionByZeroException

# ((3 + 4) * 5) % 0を計算する
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
five: NumberParseTree = NumberParseTree(5)
zero: NumberParseTree = NumberParseTree(0)
expression1: ExpressionParseTree = AdditionParseTree(three, four)
expression2: ExpressionParseTree = MultiplicationParseTree(expression1, five)
expression3: ExpressionParseTree = RemainderParseTree(expression2, zero)

print(expression3)

try:
    print(expression3.interpret())
except DivisionByZeroException as e:
    print(e)
