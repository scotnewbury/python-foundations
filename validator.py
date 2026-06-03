def validate_username(username: str) -> bool:
    return 3 <= len(username) <= 20


if __name__ == "__main__":
    print(validate_username("scot"))
    print(validate_username("so12345678901234567890"))
    print(validate_username(""))
