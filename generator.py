def element_length_calculation(list_with_words: list[str, ...]):
    list_with_len = []
    for i in list_with_words:
        if not isinstance(i, str):
            raise ValueError('The list must contain only strings')

        list_with_len.insert(0, len(i))

    return list_with_len


def generator(list_with_words: list[str, ...]) -> list[int, ...]:
    list_with_len = element_length_calculation(list_with_words)

    for j in list_with_len:
        yield j



