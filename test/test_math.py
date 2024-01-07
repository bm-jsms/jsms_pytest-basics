import pytest
import src.math as math

def test_add():
    result = math.add(5, 5)
    assert result == 10

def test_subtract():
    result = math.subtract(10, 5)
    assert result == 5

def test_multiply():
    result = math.multiply(5, 5)
    assert result == 25

def test_divide():
    result = math.divide(10, 2)
    assert result == 5