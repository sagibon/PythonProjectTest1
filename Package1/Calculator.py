# class Calculator

class Calculator:
    """the class calculator includes methods that calculate 2 numbers"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum_numbers(self):
        """Returns the sum of 2 numbers """
        return self.a + self.b

# calc = Calculator(3, 4)
# print(calc.sum_numbers())
