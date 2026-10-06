import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_greet_returns_greeting(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
