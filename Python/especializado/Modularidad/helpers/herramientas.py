def greet(name, age, gender):
  return f"Hello, my name is {name}, I am {age} years old and I am {gender}."

def calculate_circle_area(radius):
  import math
  return math.pi * radius ** 2


if __name__ == "__main__":
  print(greet("Jesus", 30, "male"))
  print(f"el area del circulo de radio 15: {calculate_circle_area(5)}  ")