def sum(num1, num2):
    return num1 + num2
  
def subtract(num1, num2):
    return num1 - num2
  
def multiply(num1, num2):
    return num1 * num2
  
def divide(num1, num2):
    if num2 == 0:
        raise ValueError("No puedes dividir entre 0")
    return num1 / num2