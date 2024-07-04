class NumberParseTree():
    num: int = 0
    def __init__(self, n: int) -> None:
        self.num = n
    def __str__(self) -> str:
        return str(self.num)

class UnaryMinusParseTree():
    def __init__(self, expression: NumberParseTree) -> None:
        self.expression = expression
    def __str__(self) -> str:
        return f'(-{str(self.expression)})'

class AdditionParseTree():
    def __init__(self, expression1: NumberParseTree, expression2: NumberParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({str(self.expression1)} + {str(self.expression2)})'

class SubtractionParseTree():
    def __init__(self, expression1: NumberParseTree, expression2: NumberParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({str(self.expression1)} - {str(self.expression2)})'

class MultiplicationParseTree():
    def __init__(self, expression1: NumberParseTree, expression2: NumberParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({str(self.expression1)} * {str(self.expression2)})'

class DivisionParseTree():
    def __init__(self, expression1: NumberParseTree, expression2: NumberParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({str(self.expression1)} / {str(self.expression2)})'

class RemainderParseTree():
    def __init__(self, expression1: NumberParseTree, expression2: NumberParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({str(self.expression1)} % {str(self.expression2)})'

class LessThanParseTree():
    def __init__(self, expression1: NumberParseTree, expression2: NumberParseTree) -> None:
        self.expression1 = expression1
        self.expression2 = expression2
    def __str__(self) -> str:
        return f'({str(self.expression1)} < {str(self.expression2)})'
