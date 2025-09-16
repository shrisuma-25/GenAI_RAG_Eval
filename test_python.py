# pip install pytest
# pytest -v

def addition(a, b):
    return a + b

#Unit Testing
def test_addition_1():
    a = 2
    b = 3
    expected = 5
    actual = addition(a, b) # 6
    assert actual == expected, f"Expected {a} + {b} to equal {expected}, but got {actual}"

# def test_addition_2():
#     a = -1
#     b = 1
#     expected = 0
#     actual = addition(a, b)

#     assert  actual == expected, "Expected -1 + 1 to equal 0"

def division(a, b):
    if b==0:
        raise ValueError("Denominator cannot be zero")
    return a / b

# Create 2 testcases
# 1. test case for 2 positive numbers
def test_divide_positiveNum():
    a = 6
    b = 2
    expected = 3
    actual = division(a, b)
    assert actual == expected, f"Expected {a} / {b} to equal {expected}, but got {actual}"

#2 . test case for division by zero
def test_division_zero():
    a = 10
    b = 0
    try:
        division(a, b)
        assert False, "Expected ValueError when dividing by zero, but no error was raised"
    except ValueError as e:
        assert str(e) == "Denominator cannot be zero", f"Expected ValueError message to be 'Denominator cannot be zero', but got '{str(e)}'"    


