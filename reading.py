from words import count_words


def reading_time(text: str, words_per_minute: int = 200) -> int:
    if words_per_minute < 1:
        raise ValueError("words_per_minute must be at least 1")
    words = count_words(text)
    return (words + words_per_minute - 1) // words_per_minute
