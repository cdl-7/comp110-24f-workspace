"""File 2/3 for Challenge Question 4"""

__author__ = "730742183"


def get_coords(xs: str, ys: str) -> None:
    i = 0  # initializes counter for first while loop
    while i < len(xs):
        x = xs[i]  # iterates through each char in xs
        j = 0  # initializes counter for second while loop
        while j < len(ys):
            y = ys[j]  # iterates through each char in ys
            print(f"({x},{y})")
            j += 1
        i += 1
