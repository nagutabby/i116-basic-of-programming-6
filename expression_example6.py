from parse_tree import ExpressionParseTree, NumberParseTree, LessThanParseTree, EqualsParseTree, OrParseTree

# 5 < 5 || 5 = 5 を計算する
five: NumberParseTree = NumberParseTree(5)
expression1: ExpressionParseTree = LessThanParseTree(five, five)
expression2: ExpressionParseTree = EqualsParseTree(five, five)
expression3 = OrParseTree(expression1, expression2)

print(expression3)
print(expression3.interpret())
