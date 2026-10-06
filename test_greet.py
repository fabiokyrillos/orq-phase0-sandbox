import unittest

from greet import greet


class GreetTest(unittest.TestCase):
    def test_returns_greeting(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
