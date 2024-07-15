from parse_tree import *

# (1 + 2) * 3 < 100
one = NumberParseTree(1)
two = NumberParseTree(2)
three = NumberParseTree(3)
one_hundred = NumberParseTree(100)

expression1: ExpressionParseTree = AdditionParseTree(one, two)
expression2: ExpressionParseTree = MultiplicationParseTree(expression1, three)
expression3: ExpressionParseTree = LessThanParseTree(expression2, one_hundred)

print(expression3)
print(expression3.interpret())

# 1 && (3 % 2 == 0)
zero = NumberParseTree(0)

expression1 = RemainderParseTree(three, two)
expression2 = EqualsParseTree(expression1, zero)
expression3 = AndParseTree(one, expression2)

print(expression3)
print(expression3.interpret())

# 2 > 3 || 2 / 3
expression1 = GreaterThanParseTree(two, three)
expression2 = DivisionParseTree(two, three)
expression3 = OrParseTree(expression1, expression2)

print(expression3)
print(expression3.interpret())
