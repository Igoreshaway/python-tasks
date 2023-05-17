unconverted_string = 'Привет!!!!'


def get_converted_string_using_replace(unconverted_string: str, replaceable_char, target_char):
    return unconverted_string.replace(replaceable_char, target_char)


def get_converted_string_using_loop(unconverted_string: str, replaceable_char, target_char):
    converted_string = ''
    for char in unconverted_string:
        if char != replaceable_char:
            converted_string += char
        else:
            converted_string += target_char
    return converted_string


def get_converted_string_using_split_and_join(unconverted_string: str, replaceable_char, target_char):
    unconverted_chars = unconverted_string.split(replaceable_char)
    result = target_char.join(unconverted_chars)
    return result


converted_string_replace = get_converted_string_using_replace(unconverted_string, '!', '?')
print(f'replace: {converted_string_replace}')
print()
converted_string_loop = get_converted_string_using_loop(unconverted_string, '!', '?')
print(f'loop: {converted_string_loop}')
print()
converted_string_split_and_join = get_converted_string_using_split_and_join(unconverted_string, '!', '?')
print(f'split and join {converted_string_split_and_join}')
