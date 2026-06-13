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
