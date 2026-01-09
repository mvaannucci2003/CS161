from datetime import datetime
# Marc Vannucci
# CS 161
# Project 1

# Step 1
pet_name = "Luna"
pet_type = "Cat"

print(f"My pet's name is {pet_name} and she is a {pet_type}.")


# Step 2
print("Enter your name:")
name = input()
print("Enter your age:")
age = input()
print("What is your yearly savings:")
savings = input("$")

older = int(age) + 10
more_savings = int(savings) * 5
monthly_savings = int(savings) / 12


print(f"Hello, {name}! You are currently {age} years old.")
print(f"in 10 years, you will be {older} years old.")
print(
    f"If you save ${savings} each year, in 5 years, you will have saved ${more_savings}."
)
print(f"your monthly savings is ${monthly_savings}.")


# Step 3
date = datetime(1970, 2, 1, 0, 0)
epoch_time = datetime(1970, 1, 1)

sec = (date - epoch_time)
print('Datetime to seconds since epoch:', sec.total_seconds())

#step 4
print('Enter egg count:')
count = input()

total = int(count)
dozen = total // 12
remainder = total % 12
print(f'This makes {dozen} dozen eggs with {remainder} left over.')
