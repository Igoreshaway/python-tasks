def check_palindrome(check_string: str) -> bool:
    reversed_string = ''.join(reversed(check_string))
    if check_string == reversed_string:
        return True
    return False


