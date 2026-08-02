from word_counter import (
    count_words,
    top_n_words,
)


class TestCountWords:
    def test_count_words_strips_punctuation(self):
        text = "May the force be with you, always!"
        result = count_words(text)
        assert "you" in result
        assert "always" in result

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


class TestTopNWords:
    def test_top_n_words_returns_correct_count(self):
        freq = {"the": 5, "cat": 3, "dog": 1}
        result = top_n_words(freq, 2)
        assert len(result) == 2
        assert result[0][0] == "the"  # most common first
        assert result[1][0] == "cat"
