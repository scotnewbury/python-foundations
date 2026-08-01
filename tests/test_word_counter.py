from word_counter import (
    count_words,
)


class TestCountWords:
    def test_count_words_strips_punctuation(self):
        text = "May the force be with you, always!"
        result = count_words(text)
        assert all(
            key == key.strip(".,!?;:'\"") for key in result.keys()
        ), "Not all keys are stripped of punctuation"

    def test_count_words_excludes_empty_keys(self):
        text = ".,!?;:'\""
        result = count_words(text)
        assert result == {}

    def test_count_words_is_lowercase(self):
        text = "This is The Way"
        result = count_words(text)
        assert all(
            key == key.lower() for key in result.keys()
        ), "Not all keys are lowercase"

    def test_count_words_basic(self):
        text = "the cat sat on the mat"
        result = count_words(text)
        assert result["the"] == 2
        assert result["cat"] == 1

    def test_count_words_empty(self):
        assert count_words("") == {}
