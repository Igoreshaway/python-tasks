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


def get_nesting_level(
        source_dict: dict, nesting_level: int = 0
) -> dict[str, int]:

    keys_and_numbers_nesting_levels = {}

    for key, value in source_dict.items():
        keys_and_numbers_nesting_levels[key] = nesting_level
        if value:
            keys_and_numbers_nesting_levels.update(
                get_nesting_level(value, nesting_level=nesting_level + 1)
            )
    return keys_and_numbers_nesting_levels


keys_with_nested_levels = get_nesting_level(content)
print(keys_with_nested_levels)
