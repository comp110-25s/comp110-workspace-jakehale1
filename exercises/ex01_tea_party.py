"""This program calculates the resources needed for a tea party."""

__author__: str = "730466172"


def main_planner(guests: int) -> None:
    """Entry point for the tea party planner, orchestrating calculations and output."""
    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    total_cost = cost(tea_count, treat_count)

    print(f"For your tea party with {guests} guests:")
    print(f"You will need {tea_count} tea bags.")
    print(f"You will need {treat_count} treats.")
    print(f"The total cost will be ${total_cost:.2f}.")


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on the number of people."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the number of teas guests will drink."""
    tea_count = tea_bags(people=people)
    return int(tea_count * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
