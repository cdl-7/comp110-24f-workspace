"""Practice with while loops"""

__author__ = "730742183"


def num_instances(phrase: str, search_char: str) -> int:
    # Returns the number of instances of search_char in phrase
    count: int = 0  # Counts instances of each char
    i: int = 0  # Index of each char
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
        i += 1
    return count
