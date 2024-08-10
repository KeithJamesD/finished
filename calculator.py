import math

x = input("Enter a number: ")
y = input("Enter another number: ")
num1 = float(x)
num2 = float(y)
operator = input("Enter an operator (+, -, *, /, ^, log, sqrt, fact): ")

def calculate(operator, num1, num2):
  if operator == "+":
    return add(num1, num2)
  elif operator == "-":
    return subtract(num1, num2)
  elif operator == "*":
    return multiply(num1, num2)
  elif operator == "/":
    return divide(num1, num2)
  elif operator == "^":
    return power(num1, num2)
  elif operator == "log":
    return logarithm(num1, num2)
  elif operator == "sqrt":
    return square_root(num1)
  elif operator == "fact":
    return factorial(num1)
  else:
    return "Invalid operator"

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def square_root(x):
  return math.sqrt(x)

def factorial(x):
  return math.factorial(x)

def power(x, y):
  return x ** y

def logarithm(x, base):
  return math.log(x, base)

calculate(operator, num1, num2)
  
result = calculate(operator, num1, num2)

print(f"The result is: {result}")
  
restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if restart == "no":
    should_end = True
    print("Goodbye")    


