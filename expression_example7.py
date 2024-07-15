from parse_tree import *

# 4 < 3 || 4 = 4 && 0 > ‐1 && (3 = 4 || 3 !=4)を計算する
zero: NumberParseTree = NumberParseTree(0)
one: NumberParseTree = NumberParseTree(1)
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
expression1: ExpressionParseTree = LessThanParseTree(four, three)
expression2: ExpressionParseTree = EqualsParseTree(four, four)
expression3: ExpressionParseTree = OrParseTree(expression1, expression2)
expression4: ExpressionParseTree = UnaryMinusParseTree(one)
expression5: ExpressionParseTree = GreaterThanParseTree(zero, expression4)
expression6: ExpressionParseTree = AndParseTree(expression3, expression5)
expression7: ExpressionParseTree = EqualsParseTree(three, four)
expression8: ExpressionParseTree = NotEqualsParseTree(three, four)
expression9: ExpressionParseTree = OrParseTree(expression7, expression8)
expression10: ExpressionParseTree = AndParseTree(expression6, expression9)

print(expression10)
print(expression10.interpret())
