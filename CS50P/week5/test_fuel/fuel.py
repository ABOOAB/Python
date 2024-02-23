import sys


def main():
    inp = input("Fraction: ")
    con = convert(inp)
    print(gauge(con))


def convert(fraction):
        while True:
            try:
                x, y = fraction.split("/")
                x = int(x)
                y = int (y)
                if x / y <= 1 :
                    return round(x / y * 100)
                else :
                    fraction = input("Fraction: ")


            except (ValueError, ZeroDivisionError):
                pass


def gauge(percentage):
    # convert the value to precent
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"
        ...


if __name__ == "__main__":
    main()
