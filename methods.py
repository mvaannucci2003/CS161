# Marc Vannucci
# HW week 4


# print(average(15, 5, 10))
# print(average(6, 20, 2))


def average(num1, num2, num3) -> float:
    """Since python is a procedural language.
    Calls to a function must by made after the function was created as you cannot call a function before it is defined.
    The script will not run in this state."""
    return (num1 + num2 + num3) / 3


def puppy_age(dog_age) -> float:
    """
    Docstring for puppy_age. Takes a number and converts to human years.

    :param dog_age: User Input
    """

    dog_years = int(dog_age)

    years = 24 + (dog_years - 2) * 4

    return f"{dog_years} dog years is equivalent to {years} human years."


print(puppy_age(input("Enter your dog's age: ")))


def car(origin, price, year) -> int:
    """
    Docstring for car takes name of the origin provided, as well as the price. And returns the value of the car given
    a certain number of years in ownership.

    :param origin: Description
    :param price: Description
    :param year: Description
    """

    if origin == "german":
        calculate = (int(price) * 0.05) * int(year)
        difference = int(price) - int(calculate)
        return (
            f"The value of the {origin} car will be ${difference} after {year} years."
        )
    elif origin == "japanese":
        calculate = (int(price) * 0.07) * int(year)
        difference = int(price) - int(calculate)
        return (
            f"The value of the {origin} car will be ${difference} after {year} years."
        )
    elif origin == "italian":
        calculate = (int(price) * 0.05) * int(year)
        difference = int(price) + int(calculate)
        return (
            f"The value of the {origin} car will be ${difference} after {year} years."
        )
    return "That is a invalid input."


print(
    car(
        input("Pick a type of car: german, japanese, italian: "),
        input("Now, what is the price: $"),
        input("What is your term length?: "),
    )
)


def puppy_calculator(dog_name, dog_age) -> str:
    """
    Docstring for puppy_age. Takes a number and converts to human years. Returns the result.

    :param dog_age: User Input
    :param dog_name: User Input
    """

    dog_years = int(dog_age)

    years = 24 + (dog_years - 2) * 4

    return f"Your {dog_name} is {years} human years old."


print(
    puppy_calculator(
        input("What is your dog's name?: "), input("Enter your dog's age: ")
    )
)


def ice_cream(request) -> float:
    """
    Docstring for ice_cream, takes the number of scoops you request and returns the cost for the ice cream
    with the cost of the cone added as well.

    :param request: Description
    :return: Description
    :rtype: float
    """

    scoops = int(request)

    cost = scoops * 1.15 + 2.25

    return f"A {scoops}-scoop cone will cost you ${cost}."


print(ice_cream(input("How many scoops would you like?: ")))
