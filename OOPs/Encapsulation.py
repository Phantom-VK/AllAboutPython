# Demonstrating Encapsulation in Python: Bank Account Example

class BankAccount:
    """
    A comprehensive example of encapsulation in a banking system.

    Encapsulation Principles Demonstrated:
    - Private attributes to protect sensitive data
    - Public methods to control access to private data
    - Data validation and protection mechanisms

    Key Benefits:
    - Prevents direct manipulation of critical data
    - Provides controlled access to internal state
    - Maintains data integrity through method-based interactions
    """

    def __init__(self, account_holder, initial_balance):
        """
        Constructor method to initialize a bank account.

        Demonstrates encapsulation through:
        - Public attribute for account holder
        - Private attribute for balance using double underscore prefix

        Args:
        - account_holder (str): Name of the account owner
        - initial_balance (float): Starting balance of the account
        """
        # Public attribute, directly accessible
        self.account_holder = account_holder

        # Private attribute, access controlled through methods
        # Double underscore (__) triggers name mangling for protection
        self.__balance = initial_balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.

        Encapsulation benefits:
        - Validates input before modifying private balance
        - Provides controlled way to change account balance
        - Prevents invalid transactions

        Args:
        - amount (float): Amount to deposit

        Returns:
        None: Prints transaction details
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.

        Encapsulation advantages:
        - Implements security checks before allowing withdrawal
        - Prevents overdrawing
        - Manages balance through a controlled interface

        Args:
        - amount (float): Amount to withdraw

        Returns:
        None: Prints transaction details or error message
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount!")

    def get_balance(self):
        """
        Controlled method to access the private balance.

        Encapsulation principle:
        - Provides read-only access to balance
        - Prevents direct manipulation
        - Allows formatting or additional logic if needed

        Returns:
        str: Formatted balance information
        """
        return f"Current balance: {self.__balance}"

    def _debug_view_balance(self):
        """
        Internal method for potential debugging (demonstrates protected method).

        Single underscore indicates this is an internal method,
        not intended for direct external use.

        Returns:
        float: Actual balance value
        """
        return self.__balance


def main():
    """
    Demonstrate the use of the BankAccount class with encapsulation.

    Shows:
    - Proper initialization
    - Controlled interactions with the account
    - Protection against direct data manipulation
    """
    # Create a bank account
    account = BankAccount("John Doe", 1000)

    # Demonstrate controlled interactions
    print(f"Account Holder: {account.account_holder}")

    # Perform transactions through controlled methods
    account.deposit(500)  # Successful deposit
    account.withdraw(200)  # Successful withdrawal

    # Attempt an invalid transaction
    account.withdraw(2000)  # Will fail due to insufficient funds

    # Retrieve balance through controlled method
    print(account.get_balance())

    # Demonstrate inability to directly access private attribute
    try:
        # This would raise an AttributeError
        print(account.__balance)
    except AttributeError as e:
        print("Cannot directly access private attribute:", e)


# Demonstrate name mangling and access protection
def demonstrate_name_mangling():
    """
    Advanced demonstration of Python's name mangling mechanism.

    Shows how Python protects private attributes through name modification.
    """
    account = BankAccount("Jane Smith", 2000)

    # Accessing the mangled name (not recommended, just for demonstration)
    print("\nName Mangling Demonstration:")
    print("Accessing balance through mangled name:")
    print(account._BankAccount__balance)  # Name mangling method, Technically possible, but not recommended


# Ensure the main functions run when the script is executed directly
if __name__ == "__main__":
    main()
    demonstrate_name_mangling()

"""
Key Encapsulation Concepts Demonstrated:
1. Private Attributes: Using double underscore (__) to create private variables
2. Controlled Access: Methods for interacting with private data
3. Data Validation: Checking conditions before modifying internal state
4. Information Hiding: Protecting sensitive information from direct manipulation
5. Interface-based Interaction: Providing clean, controlled methods for data access
"""


# Advanced Encapsulation Example (Optional)
class SecureAccount(BankAccount):
    """
    Extended example showing advanced encapsulation techniques.

    Demonstrates:
    - Inheritance
    - Additional encapsulation features
    - Enhanced data protection
    """

    def __init__(self, account_holder, initial_balance, pin):
        """
        Additional security through PIN protection.

        Args:
        - pin (str): Secret PIN for additional security
        """
        super().__init__(account_holder, initial_balance)
        self.__pin = pin  # Additional private attribute

    def verify_pin(self, entered_pin):
        """
        Secure PIN verification method.

        Demonstrates additional layer of encapsulation.

        Args:
        - entered_pin (str): PIN to verify

        Returns:
        bool: Whether the entered PIN is correct
        """
        return self.__pin == entered_pin



