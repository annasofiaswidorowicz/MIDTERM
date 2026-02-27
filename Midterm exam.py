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
def is_valid_url(url):
    if type(url) != str:
        return False
    url = url.strip()
    if url == "" or " " in url:
        return False

    if url.startswith("http://"):
        rest = url[7:]   # remove "http://"
    elif url.startswith("https://"):
        rest = url[8:]   # remove "https://"
    else:
        return False

   #Must extract the authority part
    end = len(rest)
    for sep in ["/", "?", "#"]:
        pos = rest.find(sep)
        if pos != -1 and pos < end:
            end = pos

    authority = rest[:end]
    if authority == "":
        return False  # must have a host

    # 4) Split host and port if there is a colon
    # (simplification: only one colon, so no IPv6 here)
    if ":" in authority:
        host, port_str = authority.split(":", 1)
        if host == "" or port_str == "":
            return False
        if not port_str.isdigit():
            return False
        port = int(port_str)
        if port < 1 or port > 65535:
            return False
    else:
        host = authority

    # 5) Host validation:
    # accept "localhost" OR something with dots like example.com
    if host == "localhost":
        return True

    if "." not in host:
        return False  # require a dot for domain names (class-level rule)

    parts = host.split(".")
    for part in parts:
        # each label must be non-empty
        if part == "":
            return False
        # labels cannot start or end with '-'
        if part[0] == "-" or part[-1] == "-":
            return False
        # allowed chars: letters, digits, hyphen
        for ch in part:
            if not (ch.isalnum() or ch == "-"):
                return False

    return True

tests = [
    "https://example.com",
    "http://sub.domain.com/path",
    "https://example.com:8080/a?x=1#top",
    "http://localhost:5000",
    "www.google.com",
    "https:///path",
    "https://exa mple.com",
    "https://example.com:abc",
]

for t in tests:
    print(t, is_valid_url(t))

#Question 4
def days_since_birthday_whole_years(birthday_str):
    """
    birthday_str format: "DD-MM-YYYY"
    Returns number of days passed since birthday counting ONLY full years
    (excluding birth year and current year).
    """

#It's important to know if it's a leap year, therefore:
    def is_leap(year):
        # Leap year rules:
        # - divisible by 400 -> leap
        # - divisible by 100 -> not leap
        # - divisible by 4 -> leap
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return year % 4 == 0

#Parse birthday in the format DD-MM-YYYY
    parts = birthday_str.split("-")
    birth_year = int(parts[2])

#Ask the user for today's date
    today_str = input("Enter today's date (DD-MM-YYYY): ")
    today_parts = today_str.split("-")
    current_year = int(today_parts[2])

#Count full years between birthday and today's date
    start_year = birth_year + 1
    end_year = current_year - 1

#If there are no full years in between, answer is 0
    if start_year > end_year:
        return 0

#Sum the days in each full year
    total_days = 0
    for year in range(start_year, end_year + 1):
        if is_leap(year):
            total_days += 366
        else:
            total_days += 365

    return total_days

print(days_since_birthday_whole_years("26-10-2006"))

#Question 5
def longest_word_ending_al(filename):
    longest = ""  # will store the best word found so far

#Open the file in read mode
    fp = open(filename, "r", encoding="utf-8")

    for line in fp:
        #Replace common punctuation with spaces so words separate cleanly
        line = line.replace(",", " ")
        line = line.replace(".", " ")
        line = line.replace("!", " ")
        line = line.replace("?", " ")
        line = line.replace(":", " ")
        line = line.replace(";", " ")
        line = line.replace('"', " ")
        line = line.replace("(", " ")
        line = line.replace(")", " ")

        #Split the line into words (split() handles multiple spaces)
        words = line.split()

        for w in words:
            w = w.lower()  #optional: makes matching case-insensitive

            #Check if the word ends with "al"
            if w.endswith("al"):
                #If it's longer than the current best, update
                if len(w) > len(longest):
                    longest = w

    fp.close()
    return longest

print(longest_word_ending_al("example.txt"))
