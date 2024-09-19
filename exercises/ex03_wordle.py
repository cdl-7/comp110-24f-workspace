"""Wordle using while loops"""

__author__ = "730742183"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(word_length: int) -> str:
    """Allows the user to input a word and checks if it is word_length chars long"""
    guess: str = input(f"Enter a {word_length} character word: ")
    if len(guess) == word_length:
        return guess
    else:
        while len(guess) != word_length:
            guess: str = input(f"That wasn't {word_length} chars! Try again: ")
        return guess


def contains_char(word: str, search_for: str) -> bool:
    """Searches through word to find the character designated in search_for"""
    assert len(search_for) == 1
    i: int = 0
    while i < len(word):
        if word[i] == search_for:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns a string with emojis after comparing the guess to secret_word"""
    assert len(guess) == len(secret_word)
    i: int = 0
    emojis: str = ""
    while i < len(guess):
        if guess[i] == secret_word[i]:
            emojis += GREEN_BOX
        elif contains_char(word=secret_word, search_for=guess[i]):
            # Determines if the ith letter of the secret word is in the guess
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis


def main(secret: str) -> None:
    """The main game loop"""
    turn_num: int = 1
    while turn_num <= 6:
        print(f"=== Turn {turn_num}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess=guess, secret_word=secret))
        if guess == secret:
            print(f"You won in {turn_num}/6 turns!")
            exit()
        turn_num += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
