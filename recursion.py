# Marc Vannucci
# CS 161 HW 6

x = int(input("Eneter a interger: "))
y = int(input("Enter decrease: "))
while x > 0:

    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

    x = x - y
print("blastoff!")

num_words = 0
length = True
while length:
    word = input("Enter a word: ")
    word_length = len(word)

    if word_length >= 5:
        print(f"{word} has {word_length} letters.")
        num_words += 1
        length = True

    if num_words > 5:
        print("Loser")
        length = False

    if word_length < 5:
        print("goodbye")
        length = False
summation = 10
while summation <= 100:

    print(summation, hex(summation), bin(summation))
    summation += 1


def stars(num):
    num = int(num)

    while num > 0:
        print("*" * num)
        num = num - 1


stars(input("Enter the number of stars: "))


def rec_stars(num):
    if num == 0:
        return None
    else:
        print("*" * num)
        num = num - 1
        rec_stars(num)


rec_stars(int(input("Enter a number recursively: ")))
