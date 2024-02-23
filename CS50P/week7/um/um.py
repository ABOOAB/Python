import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    my_list = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(my_list)
    ...


...


if __name__ == "__main__":
    main()
