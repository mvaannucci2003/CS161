# Marc Vannucci
# Wekk 3 HW


# Using input to prompt for username


def user(greeting: str) -> str:

    return f"Hello {greeting}"


print(user(input("What is your name? ")))


# We now prompt for the user's legal age


def user_age(age: str, adder: str) -> int:
    """The error here is that the plus sign is used to concatenate strings. You cannot
    concatenate string literals and type ints together. Be careful when using input as
    you need to convert the string to a integer first before returning."""

    element_age = int(age)
    element_adder = int(adder)
    combined = str(element_age + element_adder)

    return f"in {element_adder} years you will be {combined} years old"


print(
    user_age(input("What's your age? "), input("How many years would you like to add."))
)


def wage(hours: float, income: float) -> int:

    weekly_hours = float(hours)
    wage = float(income)

    weekly_gross = weekly_hours * wage
    annual_gross = weekly_gross * 52

    return f"Your gross pay this week is $ {weekly_gross}\nYour estimated annual gross pay will be $ {annual_gross}"


print(
    wage(
        input("Enter the number of hours worked: "),
        input("Enter the hourly wage, with the $: "),
    )
)
