import unittest
import subprocess
import sys
from pathlib import Path


COFFEE_SCRIPT = Path(__file__).resolve().parents[1] / "coffee.py"


class TestCoffeeCustomizationMessage(unittest.TestCase):
    def run_coffee_with_input(self, input_str: str) -> str:
        proc = subprocess.run(
            [sys.executable, str(COFFEE_SCRIPT)],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=5,
        )
        # combine stdout and stderr for easier debugging
        return proc.stdout + proc.stderr

    def test_single_cup_no_message(self):
        # Scenario: 1 cup ordered; the "apply to all cups" message must NOT appear
        # Inputs: name, coffee choice (2), quantity (1), size (M), then customization inputs
        inputs = """
Test User
2
1
M
1
10
1
no
none
"""
        out = self.run_coffee_with_input(inputs)
        self.assertNotIn("(This customization will apply to all cups)", out)

    def test_multiple_cups_shows_message(self):
        # Scenario: 2 cups ordered with single customization; message MUST appear
        inputs = """
    Test User
    2
    2
    no
    M
    1
    10
    1
    no
    none
    """
        out = self.run_coffee_with_input(inputs)
        self.assertIn("(This customization will apply to all cups)", out)


if __name__ == "__main__":
    unittest.main()
