import pytest
from calculator import *

# handles addition
def test_addition():
  assert add(2, 3) == 5

# handles subtraction
def test_subtraction():
  assert subtract(10, 1) == 9

# handles multiplication
def test_multiply():
  assert multiply(1, 10) == 10

# handles division
# DONE: handles zero division 
def test_divide():
  assert divide(1, 0) == "Cannot divide by 0"
  assert divide(10, 3) == 10/3
  assert divide(99,2) == 49.5

def test_get_num(monkeypatch):
  # Mock user input for valid integer
  monkeypatch.setattr('builtins.input', lambda _: "42")
  assert get_num("Enter a number: ") == 42

  # Mock user input for invalid input (non-integer)
  monkeypatch.setattr('builtins.input', lambda _: "abc")
  assert get_num(
      "Enter a number: ") == "Please enter a valid integer"

def test_get_selection(monkeypatch):
    # Mock user input for valid selection
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert get_selection() == 3

    # Mock user input for invalid selection
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(ValueError):
        get_selection()

    # Handles division by a negative number
def test_divide_negative():
  assert divide(10, -2) == -5
  assert divide(-10, -2) == 5
  assert divide(-10, 2) == -5

    # Handles division by a positive number
def test_divide_positive():
  assert divide(10, 2) == 5

    # Handles division by a floating-point number
def test_divide_float():
  assert divide(10, 3) == 10/3

    # Handles division by zero with negative dividend
def test_divide_zero_negative():
  assert divide(-10, 0) == "Cannot divide by 0"

    # Handles division by zero with positive dividend
def test_divide_zero_positive():
  assert divide(10, 0) == "Cannot divide by 0"

    # Gets a selection from user input with valid range
def test_get_selection_valid_range(monkeypatch):
  # Mock user input for valid selection
  monkeypatch.setattr('builtins.input', lambda _: "3")
  assert get_selection() == 3

  # Mock user input for invalid selection
  monkeypatch.setattr('builtins.input', lambda _: "abc")
  with pytest.raises(ValueError):
      get_selection()

    # Handles division by zero with zero dividend
def test_divide_zero_zero():
  assert divide(0, 0) == "Cannot divide by 0"


def test_get_user_input_valid_case1():
    user_input = "2 3"
    expected_values = (2, 3)
    assert get_user_input(user_input) == expected_values

def test_get_user_input_valid_case2():
    user_input = "0 -5"
    expected_values = (0, -5)
    assert get_user_input(user_input) == expected_values

def test_get_user_input_valid_case3():
    user_input = "-10 10"
    expected_values = (-10, 10)
    assert get_user_input(user_input) == expected_values

def test_get_user_input_invalid_case1():
    values_input = "2"
    with pytest.raises(ValueError) as e:
        get_user_input(values_input)
    assert str(e.value) == "Exactly 2 values should be provided."

def test_get_user_input_invalid_case2():
    values_input = "2 3 4"
    with pytest.raises(ValueError) as e:
        get_user_input(values_input)
    assert str(e.value) == "Exactly 2 values should be provided."

def test_get_user_input_invalid_case3():
    values_input = "5"
    with pytest.raises(ValueError) as e:
        get_user_input(values_input)
    assert str(e.value) == "Exactly 2 values should be provided."

