from custom_exception import DivisionByZeroException

class ExpressionParseTree():
    def __str__(self) -> str:
        return ''
    def interpret(self) -> int | float:
        return 0.0

class NumberParseTree(ExpressionParseTree):
    def __init__(self, n: int) -> None:
        self.num = n
    def __str__(self) -> str:
        return str(self.num)
    def interpret(self) -> int:
        return self.num

class UnaryMinusParseTree(ExpressionParseTree):
    def __init__(self, expression: ExpressionParseTree) -> None:
        self.expression = expression
    def __str__(self) -> str:
        return f'(-{self.expression})'
    def interpret(self) -> float:
        return -1 * self.expression.interpret()

class AdditionParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} + {self.expression2})'
    def interpret(self) -> float:
        return self.expression1.interpret() + self.expression2.interpret()

class SubtractionParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} - {self.expression2})'
    def interpret(self) -> float:
        return self.expression1.interpret() - self.expression2.interpret()

class MultiplicationParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} * {self.expression2})'
    def interpret(self) -> float:
        return self.expression1.interpret() * self.expression2.interpret()

class DivisionParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} / {self.expression2})'
    def interpret(self) -> float:
        if self.expression2.interpret() == 0:
            raise DivisionByZeroException('division by zero')
        else:
            return self.expression1.interpret() / self.expression2.interpret()

class RemainderParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} % {self.expression2})'
    def interpret(self) -> int | float:
        if self.expression2.interpret() == 0:
            raise DivisionByZeroException('division by zero')
        else:
            return self.expression1.interpret() % self.expression2.interpret()

class LessThanParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} < {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() < self.expression2.interpret():
            return 1
        else:
            return 0

class GreaterThanParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} > {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() > self.expression2.interpret():
            return 1
        else:
            return 0

class EqualsParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} = {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() == self.expression2.interpret():
            return 1
        else:
            return 0

class NotEqualsParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} != {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() != self.expression2.interpret():
            return 1
        else:
            return 0

class AndParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} && {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() == 0 or self.expression2.interpret() == 0:
            return 0
        else:
            return 1

class OrParseTree(ExpressionParseTree):
    def __init__(self, expression1: ExpressionParseTree, expression2: ExpressionParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({self.expression1} || {self.expression2})'
    def interpret(self) -> int:
        if self.expression1.interpret() == 0 and self.expression2.interpret() == 0:
            return 0
        else:
            return 1
