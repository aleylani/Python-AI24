import pytest

from shapes.rectangle import Rectangle

def test_rectangle_area():

    rect = Rectangle(5, 10)    
    assert rect.area() == 50

def test_rectangle_perimeter():

    rect = Rectangle(5, 10)
    assert rect.perimeter() == 30

def test_rectangle_is_square():

    rect = Rectangle(5, 5)
    assert rect.is_square() == True

    rect = Rectangle(5, 10)
    assert rect.is_square() == False

def test_rectangle_invalid_width():

    with pytest.raises(ValueError):
        Rectangle(-5, 10)

def test_rectangle_invalid_height():

    with pytest.raises(ValueError):
        Rectangle(5, -10)

def test_rectangle_width_setter():

    rect = Rectangle(8, 9)
    rect.width = 10

    assert rect.width == 10

def test_rectangle_height_setter():
    """This test tries changing the width of an instance, and tests it's implementation"""
    rect = Rectangle(8, 9)
    rect.height = 10

    assert rect.height == 10

