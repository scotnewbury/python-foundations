from validator import (
    add_to_history,
    validate_age,
    validate_password,
    validate_username,
)


class TestValidateUsername:
    def test_validate_username_returns_true(self):
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

    def test_password_length_is_minimum_length_returns_true(self):
        assert validate_password("Ab123456") is True

    def test_password_for_no_digits(self):
        assert validate_password("abcdeFGHIJ") is False

    def test_password_for_no_uppercase(self):
        assert validate_password("123abcdefg") is False


class TestValidateAge:
    def test_age_returns_age(self):
        assert validate_age("100") == 100

    def test_age_boundary_low_value_returns_age(self):
        assert validate_age("0") == 0

    def test_age_boundary_high_value_returns_age(self):
        assert validate_age("150") == 150

    def test_age_is_empty(self):
        assert validate_age("") is None

    def test_age_is_less_than_zero(self):
        assert validate_age("-1") is None

    def test_age_is_above_150(self):
        assert validate_age("175") is None


class TestAddToHistory:
    def test_no_history_returns_single_entry(self):
        assert add_to_history("test1") == ["test1"]

    def test_existing_history_returns_appended_list(self):
        assert add_to_history("test2", ["test1"]) == ["test1", "test2"]
