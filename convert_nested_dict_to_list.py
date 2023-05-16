source_dict = {'a': {
    'b': {
        'd': {
            'jija': 17,
            'e': None
        }
    },
    'c': None
}}


def get_unpack_dict(source_dict: dict, result=None) -> list:
    if result is None:
        result = []

    for key, value in source_dict.items():
        result.append(key)
        if not isinstance(source_dict[key], dict):
            result.append(value)
        else:
            get_unpack_dict(value, result)
    return result


unpacked_dict = get_unpack_dict(source_dict)
print(unpacked_dict)
