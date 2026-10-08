import unittest

from reading import reading_time


def _text(word_count: int) -> str:
    return " ".join(["word"] * word_count)


class ReadingTimeTests(unittest.TestCase):
    def test_reading_time_empty_text_returns_zero(self):
        self.assertEqual(reading_time(""), 0)

    def test_reading_time_whitespace_only_returns_zero(self):
        self.assertEqual(reading_time("   \t\n  "), 0)

    def test_reading_time_single_word_returns_one(self):
        self.assertEqual(reading_time(_text(1)), 1)

    def test_reading_time_exactly_one_minute(self):
        self.assertEqual(reading_time(_text(200)), 1)

    def test_reading_time_rounds_partial_minutes_up(self):
        self.assertEqual(reading_time(_text(201)), 2)

    def test_reading_time_four_hundred_words_returns_two(self):
        self.assertEqual(reading_time(_text(400)), 2)

    def test_reading_time_custom_speed(self):
        self.assertEqual(reading_time(_text(300), words_per_minute=100), 3)

    def test_reading_time_custom_speed_rounds_up(self):
        self.assertEqual(reading_time(_text(301), words_per_minute=100), 4)

    def test_reading_time_speed_of_one(self):
        self.assertEqual(reading_time(_text(5), words_per_minute=1), 5)

    def test_reading_time_zero_speed_raises(self):
        with self.assertRaises(ValueError):
            reading_time(_text(10), words_per_minute=0)

    def test_reading_time_negative_speed_raises(self):
        with self.assertRaises(ValueError):
            reading_time(_text(10), words_per_minute=-5)

    def test_reading_time_invalid_speed_raises_even_for_empty_text(self):
        with self.assertRaises(ValueError):
            reading_time("", words_per_minute=0)


if __name__ == "__main__":
    unittest.main()
