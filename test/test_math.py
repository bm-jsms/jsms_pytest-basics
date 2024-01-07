import pytest
import src.math as math

def test_add():
    assert math.add(5, 5) == 10

def test_subtract():
    assert math.subtract(10, 5) == 5

def test_multiply():
    assert math.multiply(3, 3) == 9

def test_divide():
    assert math.divide(10, 2) == 5