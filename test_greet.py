import unittest

from greet import farewell, greet


class GreetTests(unittest.TestCase):
    def test_greet_returns_greeting(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("")

    def test_farewell_returns_farewell(self):
        self.assertEqual(farewell("Ana"), "Goodbye, Ana!")

    def test_farewell_empty_name_raises(self):
        with self.assertRaises(ValueError):
            farewell("")


if __name__ == "__main__":
    unittest.main()
