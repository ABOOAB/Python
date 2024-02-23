def main():
    s = input()
    s = convert(s)
    print(s)


def convert(to):
    to = to.replace(":(", "🙁")
    to = to.replace(":)", "🙂")
    return to


main()
