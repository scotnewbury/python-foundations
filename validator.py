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


def validate_password(password: str) -> bool:
    """Check whether a password meets the format requirements.

    A valid password is 8 characters or more, contains at least one
    digit, and at least one uppercase letter.

    Args:
        password: The password string to validate.

    Returns:
        True if the password is valid, False otherwise.
    """

    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    return True


def validate_age(age_input: str) -> int | None:
    """Check whether the age meets range requirement.

    A valid age is between 0 and 150 inclusive

    Args:
        age_input: The age string to validate.

    Returns:
        The age, as an integer, if valid, otherwise None.
    """
    if not age_input.isdecimal():
        return None

    age = int(age_input)

    if not (0 <= age <= 150):
        return None

    return age


def add_to_history(entry: str, history: list[str] | None = None) -> list[str]:
    """Add an entry to the end of the history list.

    A valid entry is any string

    Args:
        entry: The entry to append to the history
        history: The list containing all past entries.

    Returns:
        The updated history list.
    """
    if history is None:
        history = []

    history.append(entry)

    return history


def normalize_username(username: str) -> str | None:
    """Update username to meet format requirements.

    Remove whitespace from the username and convert to lowercase

    Args:
        username: The username to update to match requirements.

    Returns:
        The normalize username if valid. None otherwise.
    """

    username = "".join(username.split())
    username = username.lower()

    if validate_username(username):
        return username

    return None
