# Demonstrating Object-Oriented Programming (OOP) Inheritance in Python

# Parent class (Base class) - Serves as a blueprint for basic vehicle attributes
class Vehicle:
    """
    Base class representing a generic vehicle with fundamental attributes.

    This class demonstrates the foundation of inheritance, providing
    common attributes that can be shared by different types of vehicles.

    Attributes:
    - brand (str): The manufacturer of the vehicle
    - model (str): The specific model of the vehicle
    """

    def __init__(self, brand, model):
        """
        Constructor method to initialize a Vehicle instance.

        Args:
        - brand (str): Name of the vehicle's manufacturer
        - model (str): Specific model of the vehicle
        """
        self.brand = brand  # Store the brand name
        self.model = model  # Store the model name

    def display_info(self):
        """
        Method to return a formatted string with vehicle information.

        Returns:
        str: Combination of brand and model
        """
        return f"{self.brand} {self.model}"


# Child class (Derived class) inheriting from Vehicle
class Car(Vehicle):
    """
    Specialized class representing a car, inheriting from Vehicle.

    This class demonstrates inheritance by:
    1. Inheriting attributes and methods from the parent Vehicle class
    2. Adding a new attribute specific to cars (seating_capacity)
    3. Using super() to properly initialize the parent class

    Additional Attributes:
    - seating_capacity (int): Number of seats in the car
    """

    def __init__(self, brand, model, seating_capacity):
        """
        Constructor method for Car that extends the Vehicle constructor.

        Uses super() to call the parent class's __init__ method, ensuring
        that the parent class is properly initialized before adding
        car-specific attributes.

        Args:
        - brand (str): Name of the car's manufacturer
        - model (str): Specific car model
        - seating_capacity (int): Number of seats in the car
        """
        # Call the parent class constructor using super()
        # This is crucial for proper inheritance and initialization
        super().__init__(brand, model)

        # Add car-specific attribute
        self.seating_capacity = seating_capacity

    def car_info(self):
        """
        Method to provide comprehensive car information.

        Demonstrates method extension by using the parent class's
        display_info() method and adding car-specific details.

        Returns:
        str: Detailed information about the car including brand, model, and seating capacity
        """
        return f"{self.display_info()} with seating capacity: {self.seating_capacity}"


# Practical demonstration of inheritance
def main():
    """
    Demonstrates the use of inheritance by creating a Car instance
    and displaying its information.
    """
    # Create a Car instance using the inherited and extended functionality
    car = Car("Tesla", "Model S", 5)

    # Display comprehensive car information
    print(car.car_info())  # Output: Tesla Model S with seating capacity: 5


# Ensure the main function runs when the script is executed directly
if __name__ == "__main__":
    main()

"""
Key Inheritance Concepts Demonstrated:
1. Base Class (Vehicle): Provides common attributes and methods
2. Derived Class (Car): Inherits from Vehicle and adds specific functionality
3. super() method: Properly initializes the parent class
4. Method Extension: car_info() builds upon display_info()
"""