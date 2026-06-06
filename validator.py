def validate_username(username: str) -> bool:
    if not (3 <= len(username) <= 20):
        return False
    elif username[0].isdigit():
        return False
    else:
        return True


if __name__ == "__main__":
    print(f"Username correct length: {validate_username('scot')}")
    print(f"Userrname too long: {validate_username('A12345678901234567890')}")
    print(f"Username empty: {validate_username('')}")
    print(f"Username starts with a number: {validate_username('2fortea')}")
    print(f"Username has an invalid character: {validate_username('abc$123')}")
