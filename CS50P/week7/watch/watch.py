import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if mat := re.search(r"<iframe src=(.+)></iframe>", s, re.IGNORECASE):
        if matches := re.search(
            r"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)", s, re.IGNORECASE
        ):
            return f"https://youtu.be/{matches.group(2)}"


if __name__ == "__main__":
    main()
