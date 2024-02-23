import validators


def main():
    s = input("What's your email address? ")
    if validators.email(s):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
