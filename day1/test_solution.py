import unittest
from solution import solve


class TestSolution(unittest.TestCase):
    def test_example_input(self):
        """Test with the example input from README.md"""
        password = solve("test-input.txt")
        self.assertEqual(password, 6)


if __name__ == "__main__":
    unittest.main()
