from helpers.herramientas import greet
from helpers.herramientas import calculate_circle_area as ca

def execute_calculations():
    print(greet("Bob", 25, "male"))
    radius = 10
    area = ca(radius)
    print(f"The area of a circle with radius {radius} is: {area}")

def sum_numbers(a, b):
    return a + b
  
def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
  execute_calculations()