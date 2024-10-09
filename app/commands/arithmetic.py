from app.commands import Command

class AddCommand(Command):
    def execute(self):
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 + num2
            print(f"The result of adding {num1} and {num2} is {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

class SubtractCommand(Command):
    def execute(self):
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 - num2
            print(f"The result of subtracting {num2} from {num1} is {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

class MultiplyCommand(Command):
    def execute(self):
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 * num2
            print(f"The result of multiplying {num1} and {num2} is {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

class DivideCommand(Command):
    def execute(self):
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                result = num1 / num2
                print(f"The result of dividing {num1} by {num2} is {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
