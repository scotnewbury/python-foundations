from word_counter import (
    count_words,
    filter_words,
    top_n_words,
    unique_words,
    words_by_first_letter,
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
        assert all(key == key.lower() for key in result.keys()), (
            "Not all keys are lowercase"
        )

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


class TestUniqueWords:
    def test_unique_words_basic(self):
        freq = {"the": 5, "cat": 3, "dog": 1}
        result = unique_words(freq)
        assert result == {"the", "cat", "dog"}


class TestWordsByFirstLetter:
    def test_words_by_first_letter_group_creation(self):
        freq = {"the": 5, "cat": 3, "dog": 1}
        result = words_by_first_letter(freq)
        assert result == {"t": ["the"], "c": ["cat"], "d": ["dog"]}

    def test_words_by_first_letter_add_to_existing_group(self):
        freq = {"the": 5, "cat": 3, "dog": 1, "that": 3, "this": 5}
        result = words_by_first_letter(freq)
        assert result == {"t": ["the", "that", "this"], "c": ["cat"], "d": ["dog"]}


class TestFilterWords:
    def test_filter_words_minimum_count(self):
        freq = {"the": 3, "that": 4, "start": 5}
        result = filter_words(freq, min_count=4)
        assert result == {"that": 4, "start": 5}

    def test_filter_words_minimum_length(self):
        freq = {"the": 3, "that": 4, "start": 5}
        result = filter_words(freq, min_length=4)
        assert result == {"that": 4, "start": 5}

    def test_filter_words_minimum_count_and_length(self):
        freq = {"the": 3, "that": 4, "this": 5, "start": 5}
        result = filter_words(freq, min_length=4, min_count=5)
        assert result == {"this": 5, "start": 5}

    def test_filter_words_no_length_matches(self):
        freq = {"the": 3, "that": 4, "this": 5, "start": 5}
        result = filter_words(freq, min_length=6, min_count=5)
        assert result == {}

    def test_filter_words_no_count_matches(self):
        freq = {"the": 3, "that": 4, "this": 5, "start": 5}
        result = filter_words(freq, min_length=4, min_count=6)
        assert result == {}

    def test_filter_words_empty(self):
        assert filter_words({}) == {}
