import unittest

from words import count_words


class CountWordsTests(unittest.TestCase):
    def test_count_words_mixed_whitespace(self):
        self.assertEqual(count_words("  one two  three "), 3)

    def test_count_words_single_word(self):
        self.assertEqual(count_words("hello"), 1)

    def test_count_words_tabs_and_newlines(self):
        self.assertEqual(count_words("one\ttwo\nthree"), 3)

    def test_count_words_empty_text_returns_zero(self):
        self.assertEqual(count_words(""), 0)

    def test_count_words_whitespace_only_returns_zero(self):
        self.assertEqual(count_words("   \t\n  "), 0)


if __name__ == "__main__":
    unittest.main()
