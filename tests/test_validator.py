from validator import validate_username


class TestValidateUsername:
    def test_valid_username_returns_true(self):
        assert validate_username("alice_99") is True

    def test_username_boundary_low_value_returns_true(self):
        assert validate_username("win") is True

    def test_username_boundary_high_value_returns_true(self):
        assert validate_username("a1234567890123456789") is True

    def test_username_is_empty_returns_false(self):
        assert validate_username("") is False

    def test_username_too_long_returns_false(self):
        assert validate_username("A12345678901234567890") is False

    def test_username_invalid_character_returns_false(self):
        assert validate_username("abc$123") is False

    def test_username_starting_with_number_returns_false(self):
        assert validate_username("2fortea") is False
