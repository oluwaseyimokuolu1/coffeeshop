import unittest
import subprocess
import sys
from pathlib import Path


COFFEE_SCRIPT = Path(__file__).resolve().parents[1] / "coffee.py"


class TestCoffeePowder(unittest.TestCase):
    def run_coffee_with_input(self, input_str: str) -> str:
        proc = subprocess.run(
            [sys.executable, str(COFFEE_SCRIPT)],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return proc.stdout + proc.stderr

    def test_empty_powder_defaults_none(self):
        # Single-cup path: empty powder input (press Enter) should result in 'None' topping
        inputs = """
Test User
2
1
M
1
10
1
no

"""
        out = self.run_coffee_with_input(inputs)
        self.assertIn("Topping: None", out)

    def test_invalid_then_valid_powder(self):
        # Provide an invalid selection first, then a valid 'cocoa'
        inputs = """
Test User
2
1
M
1
10
1
no
invalid
cocoa
"""
        out = self.run_coffee_with_input(inputs)
        self.assertIn("Invalid selection. Please enter 'cinnamon', 'cocoa', or 'none'", out)
        self.assertIn("Topping: Cocoa", out)


if __name__ == "__main__":
    unittest.main()
