def longest_time(h: int, m: int, s: int) -> int:
    """
    This function compares time periods and returns the longest
    :param h: number of hours
    :param m: number of minutes
    :param s: number of seconds
    :return:
    """
    if not isinstance(h, int) or not isinstance(m, int) or not isinstance(s, int):
        raise TypeError("Please enter positive integers")

    conv_h = h * 3600
    conv_min = m * 60

    time_dict = {h: conv_h, m: conv_min, s: s}
    max_value = max(time_dict.values())

    for k, v in time_dict.items():
        if max_value == v:
            return k
