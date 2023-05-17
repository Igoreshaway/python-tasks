from collections import defaultdict

string = 'aabbccdd'


def char_count_in_line(string: str) -> dict[str, int]:
    chars_and_counts = defaultdict(int)
    for i in string:
        chars_and_counts[i] += 1
    return chars_and_counts


chars_and_counts = char_count_in_line(string)
print(chars_and_counts)
