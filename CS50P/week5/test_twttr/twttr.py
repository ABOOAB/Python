def main():
    s = input("Input: ")
    print(f"Output: {shorten(s)}")
    ...


def shorten(word):
    for c in word:
        if c.lower() in ["a", "e", "i", "u", "o"]:
            word = word.replace(c, "")
    return word
    ...


if __name__ == "__main__":
    main()