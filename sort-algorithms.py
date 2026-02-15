# Marc Vannucci
# CS 161 Week 6 HW


def even_nums(low, high):
    """
    Docstring for even_nums

    :param low: starting num
    :param high: max num
    """

    even_integers = []

    for i in list(range(low, high)):
        if i % 2 == 0:
            even_integers.append(i)
    return even_integers


def even_factors(factorial):
    """
    Docstring for even_factors

    :param factorial: Positive Integer
    """
    even_divisables = []
    index = 1
    while index <= factorial:

        if factorial % index == 0:
            even_divisables.append(index)

        index += 1

    return even_divisables


def alpha_sum(name):
    """
    Docstring for alpha_sum, calculates the sum of the letter in your input based on index

    :param name: your word of choice
    """
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    user_input = list(name)
    index_sum = []

    for n in range(len(user_input)):
        for a in range(len(alphabet)):
            if user_input[n] == alphabet[a]:
                index_sum.append(a)
    total = sum(index_sum)
    return total


def rec_squares(num):
    """
    Docstring for rec_squares: calculates recursively the squares of your provided number

    :param num: number to be squared
    """

    if num == 1:
        print(1)
    else:
        rec_squares(num - 1)
        print(num**2)


def rec_high_num(integers, index):

    if index == -1:  # Base case if pivot was not found
        return -1

    if integers[index] < integers[index + 1]:  # Finds the pivot point
        return index
    else:  # Perform Reecursion
        return rec_high_num(index - 1)


def Teepee():
    nums = [12, 43, 22, 34, 2, 21, 3, 33, 81]
    peak = max(nums)
    odd_nums = []
    evens = []

    for i in nums:
        if i % 2 == 0:
            evens.append(i)

        if i % 2 != 0:
            odd_nums.append(i)

    evens.sort()
    odd_nums.sort()
    odd_nums.remove(81)
    evens.reverse()

    combined = odd_nums + [peak] + evens
    return combined


def main():
    low = int(input("What is your low range: "))
    high = int(input("What is your high range: "))

    even_numbers = even_nums(low, high)

    if even_numbers:
        print(f"Your even numbers in this range are {even_numbers}")
    else:
        print("the inputed range was invalid")

    factorial = int(input("Enter a positive number from 0-100: "))
    even_factorials = even_factors(factorial)

    if even_factors:
        print(f"The integers that are factors of {factorial} are {even_factorials}.")
    else:
        print("That was a invalid input")

    name = input("What is the name to calculate?, No Capital letters: ")

    sum_of_name = alpha_sum(name)

    if sum_of_name:
        print(f"The sum of the characters in {name} is {sum_of_name}.")

    rec_input = int(input("Enter a positive number to be squared: "))
    rec_squares(rec_input)

    print("After Teepee sort:", Teepee())

    integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = rec_high_num(integers, len(integers) - 2)
    if result:
        if result == -1:
            print("No further rearrangement exists")
        else:
            new_index = result + 1
            for i in range(result + 1, len(integers)):
                if integers[i] > integers[result] and integers[i] < integers[new_index]:
                    new_index = i
            integers[result], integers[new_index] = (
                integers[new_index],
                integers[result],
            )

            tail = integers[result + 1 :]
            tail.sort()
            integers[result + 1 :] = tail

        print(
            f"The next highest number is: {integers}"
        )  # I am not sure if I did this correctly, this one was really hard for me by far!


if __name__ == "__main__":
    main()
