

def convert_string_to_int(conv_str: str) -> int:
    """
    This function converts a string consisting of numbers to a number

    :param conv_str: string to be converted
    :return: this function returns the received number
    """
    if not conv_str.isnumeric():
        raise ValueError('Please enter a string consisting of numbers only')

    elif conv_str.isnumeric():
        res = 0
        for c in conv_str:
            res = res * 10 + ord(c) - ord('0')

        return res

