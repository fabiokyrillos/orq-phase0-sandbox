import unittest

from greet import farewell, greet, shout


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

    def test_shout_returns_shout(self):
        self.assertEqual(shout("Ana"), "HELLO, ANA!")

    def test_shout_empty_name_raises(self):
        with self.assertRaises(ValueError):
            shout("")


if __name__ == "__main__":
    unittest.main()
