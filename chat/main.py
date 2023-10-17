
from calculator import *

def calculate():
  """Performs a calculation based on user input."""

  # Get the user's input.
  operation = input("Enter the operation you want to perform (+, -, *, /): ")
  number_1 = float(input("Enter the first number: "))
  number_2 = float(input("Enter the second number: "))

  # Perform the calculation.
  if operation == "+":
    result = add(number_1, number_2)
  elif operation == "-":
    result = subtract(number_1, number_2)
  elif operation == "*":
    result = multiply(number_1, number_2)
  elif operation == "/":
    result = divide(number_1, number_2)
  else:
    print("Invalid operation.")
    return

  # Display the result.
  print(f"{number_1} {operation} {number_2} = {result}")

if __name__ == "__main__":
  calculate()
