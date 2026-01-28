from calculadora import sum, subtract, multiply, divide
import pytest

#---Test para la función suma---#
def test_positive_sum():
  assert sum(2,3) == 5
  
def test_negative_sum():
  assert sum(-2,-3) == -5
  
def test_zero_sum():
  assert sum(0,0) == 0
  
#---Test para la función resta---#
def test_positive_subtract():
  assert subtract(5,3) == 2
  
def test_negative_subtract(): 
  assert subtract(-5,-3) == -2
  
def test_zero_subtract():
  assert subtract(0,0) == 0
  
#---Test para la función multiplicación---#
def test_positive_multiply():
  assert multiply(2,3) == 6
  
def test_negative_multiply():
  assert multiply(-2,-3) == 6
  
def test_zero_multiply(): 
  assert multiply(0,0) == 0
  
#---Test para la función división---#
def test_positive_divide():
  assert divide(6,3) == 2
  
def test_float_divide():
  assert divide(7,2) == 3.5
  
def test_divide_by_zero():
  with pytest.raises(ValueError):
    divide(5,0)