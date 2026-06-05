def validate_username(username: str) -> bool:
    if not (3 <= len(username) <= 20):
        return False
    elif username == "":
        return False
    elif username[0].isdigit():
        return False
    else:
        return True


if __name__ == "__main__":
    print(validate_username("scot"))
    print(validate_username("A12345678901234567890"))
    print(validate_username(""))
    print(validate_username("2fortea"))
