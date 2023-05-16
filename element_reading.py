from collections import defaultdict

PATH_TO_FILE = './file_el'


def get_common_chars(path_to_file: str) -> list[str]:
    with open(path_to_file, 'r') as file:
        name_and_count_chars = defaultdict(int)
        for line in file:
            for char in line.replace('\n', ''):
                name_and_count_chars[char] += 1
        max_char_repetitions = max(name_and_count_chars.values())
        common_chars = []
        for char, number_of_repetitions in name_and_count_chars.items():
            if number_of_repetitions == max_char_repetitions:
                common_chars.append(char)
        return common_chars


common_char = get_common_chars(PATH_TO_FILE)
print(common_char)
