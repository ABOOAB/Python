import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments ")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments ")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    pizza = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            pizza.append(row)
    print(tabulate(pizza, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
