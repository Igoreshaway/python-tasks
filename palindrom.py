def check_palindrome(check_string: str) -> bool:
    return check_string == ''.join(reversed(check_string))


