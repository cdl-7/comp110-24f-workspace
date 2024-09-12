"""Challenge Question 01 - Practice with Conditionals"""

__author__ = "730742183"


def guess_a_number() -> None:
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == 7:
        print("You got it!")
    elif x < 7:
        print("Your guess was too low! The secret number is " + str(secret))
    elif x > 7:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
