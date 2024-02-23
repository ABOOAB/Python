from datetime import date
import re
import sys
import inflect
import operator

p = inflect.engine()


def main():
    # prompt the user to enter the date
    print(count(input("Date of Birth: ")))
    ...


# function to calculate mintues
def count(s):
    my_list = validate(s)
    # print (date.today())
    birth_day = date(int(my_list[0]), int(my_list[1]), int(my_list[2]))
    mins = (operator.__sub__(date.today(), birth_day).days) * 24 * 60
    # print(dif.days)
    ss = p.number_to_words(mins, andword="")

    return f"{ss.capitalize()} minutes"


# function to validate the correct date pattern
#                      YYYY-MM-DD
def validate(s):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d\d)$", s):
        return matches.groups()
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
