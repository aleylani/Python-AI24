import math

class Circle:

    """A class representing a circle.
    
    * param 
    
    radius: The radius of the circle.
    
    * methods
     
    .area() -> float
    Calculate and return the area of the circle 
     
    .circumference() -> float
    Calculate and return the circumference of the circle.
     
    .diameter() -> float
    Calculate and return the diameter of the circle.
     """

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number.")
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self.__radius = value

    def area(self) -> float:

        """Calculate and return the area of the circle."""

        return math.pi * self.radius ** 2
    
    def circumference(self) -> float:

        """Calculate and return the circumference of the circle."""

        return 2 * math.pi * self.radius
    
    def diameter(self) -> float:

        """Calculate and return the diameter of the circle."""

        return 2 * self.radius