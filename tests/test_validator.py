from validator import (
    validate_password,
    validate_username,
)


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


class TestValidatePassword:
    def test_validate_password_returns_true(self):
        assert validate_password("abd123DEF") is True

    def test_password_is_too_short(self):
        assert validate_password("Abc123") is False

    def test_password_for_no_digits(self):
        assert validate_password("abcdeFGHIJ") is False

    def test_password_for_no_uppercase(self):
        assert validate_password("123abcdefg") is False
