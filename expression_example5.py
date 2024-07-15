from parse_tree import ExpressionParseTree, NumberParseTree, LessThanParseTree, EqualsParseTree, OrParseTree

# 3 < 5 || 3 = 5を計算する
three: NumberParseTree = NumberParseTree(3)
five: NumberParseTree = NumberParseTree(5)
expression1: ExpressionParseTree = LessThanParseTree(three, five)
expression2: ExpressionParseTree = EqualsParseTree(three, five)
expression3: ExpressionParseTree = OrParseTree(expression1, expression2)

print(expression3)
print(expression3.interpret())
