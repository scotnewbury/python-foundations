def validate_username(username: str) -> bool:
    if not (3 <= len(username) <= 20):
        return False
    elif username[0].isdigit():
        return False
    # elif all(c.isascii() and c.isalnum() or c == "_"):
    elif not all(char.isascii() and char.isalnum() or char == "_" for char in username):
        return False
    else:
        return True


if __name__ == "__main__":
    print(f"Username correct length: {validate_username('scot')}")
    print(f"Userrname too long: {validate_username('A12345678901234567890')}")
    print(f"Username empty: {validate_username('')}")
    print(f"Username starts with a number: {validate_username('2fortea')}")
    print(
        f"Username, abc$123, has an invalid character: {validate_username('abc$123')}"
    )
    print(f"Unsername, def_456, is legal: {validate_username('def_456')}")
