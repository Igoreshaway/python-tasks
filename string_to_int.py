

def convert_string_to_int(conv_str: str) -> int:
    """
    This function converts a string consisting of numbers to a number

    :param conv_str: string to be converted
    :return: this function returns the received number
    """
    if not conv_str.isnumeric():
        raise ValueError('Please enter a string consisting of numbers only')

    if conv_str.isnumeric():
        result = 0
        for c in conv_str:
            result = result * 10 + ord(c) - ord('0')

        return result

