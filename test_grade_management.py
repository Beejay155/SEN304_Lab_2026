import pytest
from grade_management import calculate_grade

def test_grade_A():
    assert calculate_grade(75) == "A"

def test_grade_B():
    assert calculate_grade(65) == "B"

def test_grade_C():
    assert calculate_grade(55) == "C"

def test_grade_D():
    assert calculate_grade(45) == "D"

def test_grade_F():
    assert calculate_grade(30) == "F"

def test_invalid_high_score():
    with pytest.raises(ValueError):
        calculate_grade(105)

def test_invalid_low_score():
    with pytest.raises(ValueError):
        calculate_grade(-5)