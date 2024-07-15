from parse_tree import ExpressionParseTree, NumberParseTree, MultiplicationParseTree, AdditionParseTree

# 3 + 4 * 5を計算する
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
five: NumberParseTree = NumberParseTree(5)
expression1: ExpressionParseTree = MultiplicationParseTree(four, five)
expression2: ExpressionParseTree = AdditionParseTree(three, expression1)

print(three)
print(four)
print(five)
print(expression1)
print(expression2)
print(expression2.interpret())
