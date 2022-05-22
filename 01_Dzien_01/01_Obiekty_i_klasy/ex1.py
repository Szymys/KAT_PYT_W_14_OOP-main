class Calculator:
    def __init__(self) -> None:
        self.op_history = list()

    def add(self, num1, num2):
        result = num1 + num2
        self.op_history.append(f"Add {num1} to"
                               f" {num2} result is {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.op_history.append(f"Multiply {num1} *"
                               f" {num2} result is {result}")
        return result

    def print_operation(self):
        for op in self.op_history:
            print(f"{op}")


if __name__ == "__main__":
    calculator1 = Calculator()
    calculator2 = Calculator()
    print(calculator1.add(6, 6))
    calculator2.multiply(5, 0.5)
    print(calculator1.add(7, 8))
    print(calculator1.multiply(1, 2))

    calculator1.print_operation()
    calculator2.print_operation()