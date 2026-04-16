#!/usr/bin/env python3
"""
Calculator Module - A simple calculator with basic operations.

This module provides basic arithmetic operations and maintains a history
of calculations. It demonstrates different ways to include code snippets
in documentation.
"""

from datetime import datetime
from typing import List, Dict, Optional


class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.

    Attributes:
        history (List[Dict]): List of performed operations with results.
        name (str): Name of the calculator instance.
    """

    def __init__(self, name: str = "Default Calculator"):
        """
        Initialize a new Calculator instance.

        Args:
            name (str): Optional name for this calculator instance.
        """
        self.history: List[Dict] = []
        self.name = name

    # <-- add-method
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers together.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: Sum of a and b.
        """
        result = a + b
        self._save_to_history("add", a, b, result)
        return result

    # --> add-method

    # <-- subtract-method
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract second number from first number.

        Args:
            a (float): First number.
            b (float): Second number to subtract.

        Returns:
            float: Difference between a and b.
        """
        result = a - b
        self._save_to_history("subtract", a, b, result)
        return result

    # --> subtract-method

    # <-- multiply-method
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: Product of a and b.
        """
        result = a * b
        self._save_to_history("multiply", a, b, result)
        return result

    # --> multiply-method

    # <-- divide-method
    def divide(self, a: float, b: float) -> Optional[float]:
        """
        Divide first number by second number.

        Args:
            a (float): Numerator.
            b (float): Denominator.

        Returns:
            Optional[float]: Quotient of a divided by b.
                            Returns None if b is zero.
        """
        if b == 0:
            print("Error: Division by zero")
            return None
        result = a / b
        self._save_to_history("divide", a, b, result)
        return result

    # --> divide-method

    # <-- save-method
    def _save_to_history(self, operation: str, a: float, b: float, result: float) -> None:
        """
        Save calculation to history.

        Args:
            operation (str): Name of the operation performed.
            a (float): First operand.
            b (float): Second operand.
            result (float): Result of the operation.
        """
        self.history.append({
            'operation': operation,
            'operands': (a, b),
            'result': result,
            'timestamp': datetime.now().isoformat(),
            'calculator': self.name
        })

    # --> save-method

    def get_history(self) -> List[Dict]:
        """
        Return the complete calculation history.

        Returns:
            List[Dict]: List of all performed operations with their details.
        """
        return self.history

    def clear_history(self) -> None:
        """Clear all calculation history."""
        self.history.clear()


# <-- helper-function
def format_result(result: float, precision: int = 2) -> str:
    """
    Format a numeric result with specified precision.

    Args:
        result (float): Number to format.
        precision (int): Number of decimal places. Defaults to 2.

    Returns:
        str: Formatted number as string.
    """
    return f"{result:.{precision}f}"


# --> helper-function


# <-- usage-example
if __name__ == "__main__":
    # Create a calculator instance
    calc = Calculator("My Calculator")

    # Perform some calculations
    sum_result = calc.add(10, 5)
    print(f"Sum: {sum_result}")

    difference = calc.subtract(10, 5)
    print(f"Difference: {difference}")

    product = calc.multiply(10, 5)
    print(f"Product: {product}")

    quotient = calc.divide(10, 5)
    print(f"Quotient: {quotient}")

    # Show history
    print("\nCalculation History:")
    for entry in calc.get_history():
        print(f"  {entry['operation']}: {entry['operands']} = {entry['result']}")
# --> usage-example