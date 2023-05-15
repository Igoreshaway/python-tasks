content = {
    'a': {
        'b': {
            'd': {
                'e': None
            }
        },
        'c': None
    }
}


# def get_nesting_level(content: dict) -> dict[str, int]:
#     tmp = [content]
#     result = {}
#     nesting_level = 0
#     while tmp:
#         elem = tmp.pop()
#         key = str(elem.keys())
#         result[key] = nesting_level
#         nesting_level += 1
#         if type(elem) == dict:
#             for obj in elem.values():
#                 if type(obj) == dict:
#                     tmp.append(obj)
#                     # result[obj] = nesting_level
#                     # nesting_level += 1
#                 else:
#                     print(obj)
#     return result


def get_nesting_level(content: dict, result: dict = None, nesting_level: int = 0) -> dict[str, int]:
    if result is None:
        result = {}
    for_unpack = [content]
    get_elem_key = for_unpack[0].keys()
    if len(get_elem_key) > 1:
        for i in get_elem_key:
            result[i] = nesting_level
    else:
        result[str(*get_elem_key)] = nesting_level

    unpacing = for_unpack[0].pop(*get_elem_key)
    nesting_level += 1
    if unpacing is None:
        return result
    return get_nesting_level(unpacing, result, nesting_level)


key_with_nested_level = get_nesting_level(content)
print(key_with_nested_level)
