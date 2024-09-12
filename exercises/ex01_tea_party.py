"""Tea Party Exercise"""

__author__ = "730742183"


def main_planner(guests: int) -> None:
    """Calls and prints the final output for the functions below"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    # Is there a better way to write this next line?
    # (instead of calling the functions again)
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    return None


def tea_bags(people: int) -> int:
    """Determine number of tea bags per person"""
    return people * 2


def treats(people: int) -> int:
    """Determines number of treats per person"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines total cost"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
