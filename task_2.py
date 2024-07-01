import random


def get_numbers_ticket(min_: int, max_: int, quantity: int) -> list | None:
    """
    Function generates a set of unique random numbers for lotteries
    :param
        min_: minimum number
        max_: maximum number
        quantity: quantity of numbers to generate
    :return list of unique random numbers
    """
    if any([min_ < 1, max_ > 1000, max_ - min_ + 1 < quantity, min_ >= max_]):
        print("Check your input!")
        return []

    results = set()
    while len(results) < quantity:
        results.add(random.randint(min_, max_))

    results_list = sorted(list(results))
    return results_list


if __name__ == "__main__":
    result = get_numbers_ticket(0, 49, 6)
    print(result)
