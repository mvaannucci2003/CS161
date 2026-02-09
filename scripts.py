# Marc Vannucci
# Week 5 HW

import requests
import psutil


def pool_admission(age):
    """
    Docstring for pool_admission, takes the age of the visitor and returns the price they have to take for entry.

    :param age: Person's age prices below are as follows.
    """

    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    else:
        return 4


# Function for HTTP query
def request(url, target_word):

    response = requests.get(url)

    if response.status_code == 200:
        content = response.text.lower()
        word = target_word.lower()

        return content.count(word)


def main():
    # Counting Processes
    processes = len(list(psutil.process_iter()))
    print(f"Total processes working: {processes}")

    # Querying the HTTP page for Hugo
    url = "https://gohugo.io"
    target_word = "Hugo"

    occurance = request(url, target_word)
    print(
        f"The word {target_word} appeared {occurance} times at HTTP 'https://gohugo.io'."
    )

    # Process for dividing evenly by 5
    divisable = int(input("What is your number: "))

    if divisable % 5 == 0:
        print(f"{divisable} Is divisable by 5!")
    else:
        print(f"{divisable} Not divisable by 5")

    # Checking your state capital
    state = input("Enter a state: (Hint: Somewhere in the Pacific NW) ")

    if state == "Oregon":
        print("Salem")
    elif state == "California":
        print("Sacramento")
    elif state == "Washington":
        print("Olympia")
    elif state == "Arizonia":
        print("Phoenix")
    elif state == "Wisconsin":
        print("Madison")
    elif state == "Colorado":
        print("Denver")
    elif state == "Idaho":
        print("Boise")
    else:
        print("Sorry, Don't know that one. Update me!")

    dict_states = {
        "Oregon": "Salem",
        "California": "Sacramento",
        "Washington": "Olympia",
        "Arizonia": "Phoenix",
        "Wisconsin": "Madison",
        "Colorado": "Denver",
        "Idaho": "Boise",
    }

    capital = dict_states.get("Oregon", "Not found")
    print(f"Calling {capital}, the capital of Oregon from dictionary")

    # Executing a dicitonary call command
    command = "Call Oregon"

    match command:
        case "Call Oregon":
            print(
                f"Command recognized: Calling {capital}, the of Oregon from dictionary"
            )
        case _:
            print("Command not found")

    # Function call for pool entry
    age = pool_admission(int(input("What is you age? ")))
    print(f"Your cost is {age} for entry.")


if __name__ == "__main__":
    main()
