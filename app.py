
import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(40, 40), 80)

    def test_subtract(self):
        self.assertEqual(subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(multiply(6, 4), 24)


if __name__ == "__main__":

    print("Student Calculator Application")
    print("Addition:", add(20, 20))
    print("Subtraction:", subtract(20, 20))
    print("Multiplication:", multiply(20, 20))

    print("\nExecuting Automated Tests...\n")

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
