import math

class Calculator:

    def add(self, a, b):                # Function to add two numbers

        return a + b

    def subtract(self, a, b):           # Function to subtract two numbers

        return a - b

    def multiply(self, a, b):           # Function to multiply two numbers

        return a * b

    def divide(self, a, b):             # Function to divide two numbers
        if b == 0:
             raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, x):           # Function to find the square root of a number

        return math.sqrt(x)


if __name__ == "__main__":

    calculator = Calculator()                                                   # create an instance of the Calculator class
    num1 = 16
    num2 = 4
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")                    #calling the add method
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")               #calling the subtract method
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")               #calling the multiply method
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")                 #calling the divide method

    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")        #calling the square_root method