import unittest

from slug import slugify


class SlugifyTests(unittest.TestCase):
    def test_slugify_removes_accents(self):
        self.assertEqual(slugify("Olá Mundo!"), "ola-mundo")

    def test_slugify_removes_accents_from_many_letters(self):
        self.assertEqual(slugify("ação é Ótima"), "acao-e-otima")

    def test_slugify_lowercases_text(self):
        self.assertEqual(slugify("HELLO World"), "hello-world")

    def test_slugify_collapses_repeated_separators(self):
        self.assertEqual(slugify("one   two -- three"), "one-two-three")

    def test_slugify_trims_leading_and_trailing_separators(self):
        self.assertEqual(slugify("  --Hello World!!  "), "hello-world")

    def test_slugify_keeps_digits(self):
        self.assertEqual(slugify("Top 10 Songs"), "top-10-songs")

    def test_slugify_empty_text_returns_empty(self):
        self.assertEqual(slugify(""), "")

    def test_slugify_only_separators_returns_empty(self):
        self.assertEqual(slugify("  !!-- "), "")


if __name__ == "__main__":
    unittest.main()
