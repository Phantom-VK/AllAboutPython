# Demonstrating Polymorphism in Python

class Cat:
    """
    Represents a Cat with a specific sound method.

    Demonstrates how different classes can implement the same method name
    with different behaviors, a key principle of polymorphism.

    This class shows:
    - Method implementation specific to cats
    - Ability to define a sound method independently
    """

    def sound(self):
        """
        Produce the sound characteristic of a cat.

        Returns:
        str: The sound a cat makes
        """
        return "Meow"


class Dog:
    """
    Represents a Dog with a specific sound method.

    Showcases polymorphic behavior by implementing a 'sound' method
    that differs from the Cat class, but can be called in the same way.

    This class demonstrates:
    - Method implementation specific to dogs
    - Ability to have different implementations of the same method name
    """

    def sound(self):
        """
        Produce the sound characteristic of a dog.

        Returns:
        str: The sound a dog makes
        """
        return "Woof"


def make_sound(animal):
    """
    Polymorphic function that works with any object 
    that has a 'sound' method.

    Key polymorphism principles demonstrated:
    - Function doesn't care about the specific type of animal
    - Works with any object that implements a 'sound' method
    - Demonstrates runtime polymorphism

    Args:
    - animal (object): Any object with a sound() method

    Returns:
    None: Prints the sound of the animal
    """
    print(animal.sound())


def main():
    """
    Demonstrate polymorphic behavior by creating 
    different animal objects and calling the same method.

    Shows how:
    - Different objects can be treated uniformly
    - Method calls are resolved at runtime
    - Same function works with different object types
    """
    # Create instances of different classes
    cat = Cat()
    dog = Dog()

    # Demonstrate polymorphic method calls
    print("Cat sound:")
    make_sound(cat)  # Output: Meow

    print("\nDog sound:")
    make_sound(dog)  # Output: Woof


# Additional example to show polymorphism with a list of different objects
def demonstrate_polymorphic_list():
    """
    Additional example showing polymorphism with a collection of objects.

    Demonstrates how:
    - A list can contain objects of different types
    - The same method can be called on each object
    - Each object responds according to its own implementation
    """
    print("\nPolymorphism with a list of animals:")
    animals = [Cat(), Dog(), Cat(), Dog()]

    for animal in animals:
        make_sound(animal)


# Ensure the main functions run when the script is executed directly
if __name__ == "__main__":
    main()
    demonstrate_polymorphic_list()

"""
Key Polymorphism Concepts Demonstrated:
1. Method Overriding: Different classes implement the same method name
2. Runtime Polymorphism: Method calls resolved at runtime
3. Duck Typing: Objects are used based on their methods, not their type
4. Flexible Function Design: make_sound() works with any object having a sound() method
"""


# Advanced Polymorphism Example (Optional Exploration)
class Bird:
    def sound(self):
        return "Chirp"


# This shows how easily new classes can be added without changing existing code
def explore_polymorphism():
    """
    Demonstrates how polymorphism allows easy extension of the system.

    Shows that:
    - New classes can be added seamlessly
    - The existing make_sound() function works without modification
    """
    bird = Bird()
    print("\nAdding a new animal (Bird):")
    make_sound(bird)  # Output: Chirp