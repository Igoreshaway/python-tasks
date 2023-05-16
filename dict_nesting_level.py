content = {
    'a': {
        'b': {
            'd': {
                'e': None
            }
        },
        'c': None,
    }
}


# def get_nesting_level(content: dict, result: dict = None, nesting_level: int = 0) -> dict[str, int]:
#     if result is None:
#         result = {}
#     for_unpack = [content]
#     get_elem_key = for_unpack[0].keys()
#
#     if len(get_elem_key) > 1:
#         for i in get_elem_key:
#             result[i] = nesting_level
#     else:
#         result[str(*get_elem_key)] = nesting_level
#
#     unpacing = for_unpack[0].pop(*get_elem_key)
#     nesting_level += 1
#     if unpacing is None:
#         return result
#     return get_nesting_level(unpacing, result, nesting_level)

def get_nesting_level(source_dict: dict, dict_with_number_nesting_level: dict = None, nesting_level: int = 0) -> dict[
    str, int]:
    if dict_with_number_nesting_level is None:
        dict_with_number_nesting_level = {}

    for key, value in source_dict.items():
        dict_with_number_nesting_level[key] = nesting_level
        if len(key) > 1:
            for nesting_key in source_dict.keys():
                dict_with_number_nesting_level[nesting_key] = nesting_level
        if value:
            get_nesting_level(value, dict_with_number_nesting_level, nesting_level=nesting_level + 1)
    return dict_with_number_nesting_level


key_with_nested_level = get_nesting_level(content)
print(key_with_nested_level)
