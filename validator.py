def validate_username(username: str) -> bool:
    """Check whether a username meets the format requirements.

    A valid username is 3 to 20 characters, contains only letters,
    numbers, and underscores, and does not start with a number.

    Args:
        username: The username string to validate.

    Returns:
        True if the username is valid, False otherwise.
    """

    if not (3 <= len(username) <= 20):
        return False

    if username[0].isdigit():
        return False

    if not all((char.isascii() and char.isalnum()) or char == "_" for char in username):
        return False

    return True


if __name__ == "__main__":
    print(f"Username correct length: {validate_username('scot')}")
    print(f"Username too long: {validate_username('A12345678901234567890')}")
    print(f"Username empty: {validate_username('')}")
    print(f"Username starts with a number: {validate_username('2fortea')}")
    print(
        f"Username, abc$123, has an invalid character: {validate_username('abc$123')}"
    )
    print(f"Username, def_456, is legal: {validate_username('def_456')}")
