

def longest_time(h: int, m: int, s: int) -> int:
    """
    This function compares time periods and returns the longest
    :param h: number of hours
    :param m: number of minutes
    :param s: number of seconds
    :return:
    """
    if type(h) != int or type(m) != int or type(s) != int:
        raise ValueError("Please enter positive integers")

    elif type(h) == int or type(m) == int or type(s) == int:
        conv_h = h * 3600
        conv_min = m * 60

        list_with_sec = [conv_h, conv_min, s]
        max_value = max(list_with_sec)

        if max_value == conv_h:
            return h
        elif max_value == conv_min:
            return m
        else:
            return s
