import sys


def main():
    # check number of commend line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # check if the file not a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    print(lines(sys.argv[1]))


def lines(argv):
    counter = 0
    with open(argv, "r") as file:
        while True:
            try:
                row = file.readline()

                # check the end of the file
                if not row:
                    return counter
                # check if the line start with (#) or space
                if row.lstrip().startswith("#") or row.isspace() == True:
                    continue
                else:
                    counter = counter + 1
            #  the end of the file // when he can't get line//
            except:
                break


if __name__ == __name__:
    main()
