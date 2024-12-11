# Demonstrating Abstract Base Classes (ABC) in Python

# Import ABC (Abstract Base Class) and abstractmethod decorator
from abc import ABC, abstractmethod


# Abstract base class defining a template for geometric shapes
class Shape(ABC):
    """
    Abstract base class that serves as a blueprint for geometric shapes.

    This class demonstrates the concept of abstract base classes in Python:
    - Uses ABC (Abstract Base Class) to create a template
    - Defines abstract methods that MUST be implemented by child classes
    - Ensures a consistent interface for all shape-related classes

    Key Characteristics:
    - Cannot be instantiated directly
    - Requires child classes to implement all abstract methods
    - Provides a standardized structure for shape-related classes
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of a shape.

        This method MUST be implemented by any non-abstract child class.
        Raises an error if a child class does not override this method.

        Returns:
        float: The calculated area of the shape
        """
        pass  # Placeholder for mandatory method implementation

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of a shape.

        This method MUST be implemented by any non-abstract child class.
        Raises an error if a child class does not override this method.

        Returns:
        float: The calculated perimeter of the shape
        """
        pass  # Placeholder for mandatory method implementation


# Concrete class implementing the abstract Shape class
class Rectangle(Shape):
    """
    Concrete implementation of the Shape abstract base class for rectangles.

    Demonstrates how to:
    - Inherit from an abstract base class
    - Implement all required abstract methods
    - Provide specific implementation for rectangle calculations

    Attributes:
    - length (float): Length of the rectangle
    - breadth (float): Width of the rectangle
    """

    def __init__(self, length, breadth):
        """
        Constructor to initialize a Rectangle instance.

        Args:
        - length (float): Length of the rectangle
        - breadth (float): Width of the rectangle
        """
        self.length = length  # Store the length of the rectangle
        self.breadth = breadth  # Store the width of the rectangle

    def area(self):
        """
        Calculate the area of the rectangle.

        Overrides the abstract area() method from the Shape class.

        Returns:
        float: Area of the rectangle (length * breadth)
        """
        return self.length * self.breadth

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Overrides the abstract perimeter() method from the Shape class.

        Returns:
        float: Perimeter of the rectangle (2 * (length + breadth))
        """
        return 2 * (self.length + self.breadth)


def main():
    """
    Demonstrate the usage of the abstract base class and concrete implementation.

    Shows how to:
    - Create an instance of a concrete shape class
    - Call implemented methods
    - Calculate area and perimeter
    """
    # Create a rectangle instance
    rect = Rectangle(10, 20)

    # Calculate and display area and perimeter
    print("Area:", rect.area())  # Output: Area: 200
    print("Perimeter:", rect.perimeter())  # Output: Perimeter: 60


# Ensure the main function runs when the script is executed directly
if __name__ == "__main__":
    main()

"""
Key Abstract Base Class (ABC) Concepts Demonstrated:
1. Creating an abstract base class with mandatory method implementations
2. Using @abstractmethod decorator to enforce method implementation
3. Providing a consistent interface for derived classes
4. Ensuring that all child classes provide specific implementations
5. Preventing direct instantiation of the abstract base class
"""

# Uncomment the following lines to demonstrate ABC constraints
# Attempting to instantiate the abstract base class will raise an error
# shape = Shape()  # This would raise a TypeError

# Attempting to create a class without implementing all abstract methods will also raise an error
# class Circle(Shape):
#     def area(self):
#         return 3.14 * self.radius ** 2
#     # Missing perimeter() implementation would prevent instantiation