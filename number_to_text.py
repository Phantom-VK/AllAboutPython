class NumberToTextConverter:
    """
    A class to convert numbers into Indian text format and save results to files.
    Supports numbers up to crores (10,000,000).
    """

    def __init__(self):
        # Define basic number words
        self.ones = [
            "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"
        ]

        self.tens = [
            "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
        ]

        # Indian numbering system units
        self.indian_units = [
            (10000000, "crore"),
            (100000, "lakh"),
            (1000, "thousand"),
            (100, "hundred")
        ]

    def convert_hundreds(self, num):
        """Convert numbers less than 1000 to text"""
        if num == 0:
            return ""

        result = ""

        # Handle hundreds
        if num >= 100:
            result += self.ones[num // 100] + " hundred"
            num %= 100
            if num > 0:
                result += " and "

        # Handle tens and ones
        if num >= 20:
            result += self.tens[num // 10]
            if num % 10 > 0:
                result += " " + self.ones[num % 10]
        elif num > 0:
            result += self.ones[num]

        return result

    def number_to_text(self, number):
        """
        Convert a number to Indian text format
        Args:
            number (int): The number to convert
        Returns:
            str: Text representation of the number
        """
        if not isinstance(number, int) or number < 0:
            return "Invalid number"

        if number == 0:
            return "zero"

        result = ""

        # Process each unit (crore, lakh, thousand, hundred)
        for value, unit in self.indian_units:
            if number >= value:
                quotient = number // value
                if unit == "crore" or unit == "lakh":
                    # For crore and lakh, we can have multiple digits
                    unit_text = self.convert_hundreds(quotient)
                else:
                    # For thousand and hundred, use convert_hundreds
                    unit_text = self.convert_hundreds(quotient)

                if unit_text:
                    result += unit_text + " " + unit
                    number %= value
                    if number > 0:
                        result += " "

        # Handle remaining number (less than 100)
        if number > 0:
            remaining_text = self.convert_hundreds(number)
            result += remaining_text

        return result.strip().title()

    def convert_multiple_numbers(self, numbers):
        """
        Convert multiple numbers to text format
        Args:
            numbers (list): List of numbers to convert
        Returns:
            list: List of tuples (number, text_representation)
        """
        results = []
        for num in numbers:
            text = self.number_to_text(num)
            results.append((num, text))
        return results

    def save_to_file(self, numbers, filename="number_conversions.txt"):
        """
        Convert numbers to text and save to a file
        Args:
            numbers (list): List of numbers to convert
            filename (str): Name of the output file
        """
        try:
            conversions = self.convert_multiple_numbers(numbers)

            with open(filename, 'w', encoding='utf-8') as file:
                file.write("Number to Text Conversions\n")
                file.write("=" * 50 + "\n\n")

                for number, text in conversions:
                    # Format number with Indian comma system
                    formatted_number = self.format_indian_number(number)
                    file.write(f"{formatted_number} -> {text}\n")

                file.write(f"\nTotal conversions: {len(conversions)}\n")

            print(f"Successfully saved {len(conversions)} conversions to '{filename}'")
            return True

        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def format_indian_number(self, number):
        """
        Format number with Indian comma system (e.g., 1,23,000)
        Args:
            number (int): Number to format
        Returns:
            str: Formatted number string
        """
        if number < 1000:
            return str(number)

        num_str = str(number)
        if len(num_str) <= 3:
            return num_str

        # Add commas in Indian format
        result = ""
        num_str = num_str[::-1]  # Reverse for easier processing

        for i, digit in enumerate(num_str):
            if i == 3 or (i > 3 and (i - 3) % 2 == 0):
                result = "," + result
            result = digit + result

        return result

    def display_conversions(self, numbers):
        """
        Display number conversions in console
        Args:
            numbers (list): List of numbers to convert and display
        """
        print("Number to Text Conversions:")
        print("=" * 50)

        conversions = self.convert_multiple_numbers(numbers)
        for number, text in conversions:
            formatted_number = self.format_indian_number(number)
            print(f"{formatted_number} -> {text}")


# Example usage and testing
def main():
    """Demonstrate the NumberToTextConverter class"""

    # Create converter instance
    converter = NumberToTextConverter()

    # Test numbers from the examples
    test_numbers = [123000, 145678, 567, 1, 25, 100, 1000, 50000, 500000, 1000000]

    print("Testing Number to Text Converter")
    print("=" * 40)

    # Display conversions in console
    converter.display_conversions(test_numbers)

    print("\n" + "=" * 40)

    # Save to file
    converter.save_to_file(test_numbers, "converted_numbers.txt")

    # Test individual conversions
    print("\nIndividual Tests:")
    print(f"123000 -> {converter.number_to_text(123000)}")
    print(f"145678 -> {converter.number_to_text(145678)}")
    print(f"567 -> {converter.number_to_text(567)}")


if __name__ == "__main__":
    main()