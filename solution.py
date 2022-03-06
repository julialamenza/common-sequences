#!/usr/bin/env python3

import fileinput
import re

MOST_COMMON = 100
WORD_SEQ = 3

dict_count = {}
regex = r"(?!('|’).*('|’))\b[\w('|’)]+\b"


def print_result(dict_count: dict[str, int]) -> None:
    sorted_dict = {
        k: v
        for k, v in sorted(dict_count.items(), key=lambda item: item[1], reverse=True)
    }
    for k, v in list(sorted_dict.items())[:MOST_COMMON]:
        print(f"{k} - {v}")
    pass


def process(line: str, last_words: list[str]) -> list[str]:
    matches = re.finditer(regex, line)

    for index, match in enumerate(matches):
        word = match.group()
        if len(last_words) == WORD_SEQ - 1:
            three_words = " ".join([*last_words, word])
            if three_words not in dict_count:
                dict_count[three_words] = 1
            else:
                dict_count[three_words] = dict_count[three_words] + 1
            last_words.pop(0)
        last_words.append(word)

    return last_words


if __name__ == "__main__":
    current_file = None
    last_words = []
    for line in fileinput.input():
        now_processing = fileinput.filename()
        if now_processing != current_file:
            current_file = now_processing
            print_result(dict_count)
            print(f"Now processing file {now_processing}")
            dict_count = {}
            last_words = []
        last_words = process(line.lower(), last_words)
    print_result(dict_count)
