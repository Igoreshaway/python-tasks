from collections import defaultdict

test_text = 'Привет я Игорёша привет я катя'


def get_longest_and_common_words(text: str) -> tuple[list[str], list[str]]:
    longest_words = []
    words_and_counts = defaultdict(int)
    words_text = text.split()
    max_len_words = max(words_text, key=len)
    max_count_repeat_word = 0
    for word in words_text:
        word = word.lower()
        words_and_counts[word] += 1
        if len(word) == len(max_len_words):
            longest_words.append(word)
        if max_count_repeat_word < words_text.count(word):
            max_count_repeat_word = words_text.count(word)

    result_list = []

    for word, count_repeat in words_and_counts.items():
        if count_repeat == max_count_repeat_word:
            result_list.append(word)
    return longest_words, result_list


longest_words, common_words = get_longest_and_common_words(test_text)

print(f'longest words: {longest_words}')
print(f'common words: {common_words}')
