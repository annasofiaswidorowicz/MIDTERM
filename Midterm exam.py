#Question 1
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
    for i in range(len(random_numbers)):
        if random_numbers[i] % 2 != 0:  # odd number
            random_numbers[i] = -random_numbers[i]
        else:  # even number
            random_numbers[i] = random_numbers[i] * 2

    print(random_numbers)

#Question 2
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def palindrome(word):
    # A palindrome reads the same forwards and backwards
    return word == word[::-1]

options = [
    "6800923757255865070000705685527573290086",
    "1414884937242655719669145562427394884141",
    "9847255590886266818998186626880955527489",
    "6892149109325320763773670235239019412986"
]

for s in options:
    # Print each option and whether it is a palindrome
    print(s, palindrome(s))

#Question 3
