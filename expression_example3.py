from parse_tree import ExpressionParseTree, NumberParseTree, AdditionParseTree, MultiplicationParseTree, DivisionParseTree

# ((3 + 4) * 5) / 3を計算する
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
five: NumberParseTree = NumberParseTree(5)
expression1: ExpressionParseTree = AdditionParseTree(three, four)
expression2: ExpressionParseTree = MultiplicationParseTree(expression1, five)
expression3: ExpressionParseTree = DivisionParseTree(expression2, three)

print(expression3)
print(expression3.interpret())
