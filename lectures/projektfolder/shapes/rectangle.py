class Rectangle:
    """Class for creating and manipulating rectangles."""

    def __init__(self, width: int | float, height: int | float) -> None:
        """
        Initialize a rectangle with width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int | float:
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int | float) -> None:
        """Set the width of the rectangle."""
        if value <= 0:
            raise ValueError("Width must be positive.")
        self.__width = value

    @property
    def height(self) -> int | float:
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value: int | float) -> None:
        """Set the height of the rectangle."""
        if value <= 0:
            raise ValueError("Height must be positive.")
        self.__height = value

    def area(self) -> int | float:
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> int | float:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return self.width == self.height