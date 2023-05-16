source_dict = {'a': {
    'b': {
        'd': {
            'jija': 17,
            'e': None
        }
    },
    'c': None,
}}


# {
#     ('a', 'b', 'd', 'jija'): 17,
#     ('a', 'b', 'd', 'e'): None,
#     ('c',): None,
# }


def get_dict_with_tuples(source_dict, keys=None, result=None):
    if keys is None:
        keys = []

    if result is None:
        result = {}

    for key, value in source_dict.items():
        if not isinstance(value, dict):
            result[tuple(keys + [key])] = value
            yield result
        else:
            yield from get_dict_with_tuples(value, keys + [key], result)

dict_with_tuple = get_dict_with_tuples(source_dict)
print(next(dict_with_tuple))
print(next(dict_with_tuple))
print(next(dict_with_tuple))



