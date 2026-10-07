import unittest

from initials import initials


class InitialsTests(unittest.TestCase):
    def test_initials_multiple_names(self):
        self.assertEqual(initials("ana maria souza"), "AMS")

    def test_initials_handles_repeated_whitespace(self):
        self.assertEqual(initials("ana   maria\tsouza"), "AMS")

    def test_initials_single_name(self):
        self.assertEqual(initials("ana"), "A")

    def test_initials_already_uppercase(self):
        self.assertEqual(initials("ANA MARIA"), "AM")

    def test_initials_empty_text_returns_empty(self):
        self.assertEqual(initials(""), "")

    def test_initials_whitespace_only_returns_empty(self):
        self.assertEqual(initials("   "), "")


if __name__ == "__main__":
    unittest.main()
