from collections import defaultdict

PATH_TO_FILE = './file_el'


def get_common_chars(path_to_file: str) -> list[str]:
    with open(PATH_TO_FILE, 'r') as file:
        name_and_count_chars = defaultdict(int)
        for line in file:
            line_without_break_char = line.replace('\n', '')
            for char in line_without_break_char:
                name_and_count_chars[char] += 1
        max_value_char_repetitions = max(name_and_count_chars.values())
        common_chars = []
        for char, number_of_repetitions in name_and_count_chars.items():
            if number_of_repetitions == max_value_char_repetitions:
                common_chars.append(char)
        return common_chars


common_char = get_common_chars(PATH_TO_FILE)
print(common_char)
