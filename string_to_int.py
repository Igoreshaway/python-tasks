

def convert_string_to_int(convertible_string: str) -> int:
    """
    This function converts a string consisting of numbers to a number

    :param conv_str: string to be converted
    :return: this function returns the received number
    """
    if not convertible_string.isnumeric():
        raise ValueError('Please enter a string consisting of numbers only')

    result = 0
    for c in convertible_string:
        result = result * 10 + ord(c) - ord('0')

    return result
