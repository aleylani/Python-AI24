# tests/test_circle.py
import pytest
from shapes.circle import Circle
import math

def test_circle_area():
    circ = Circle(3)
    assert math.isclose(circ.area(), 28.274333882308138, rel_tol=1e-9)

def test_circle_circumference():
    circ = Circle(3)
    assert math.isclose(circ.circumference(), 18.84955592153876, rel_tol=1e-9)

def test_circle_diameter():
    circ = Circle(3)
    assert circ.diameter() == 6

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(-5)
        

def test_circle_setters_should_change_radius_attribute():
    circ = Circle(5)
    circ.radius = 10
    assert circ.radius == 10
