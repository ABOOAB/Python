def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m) / 60
    return h + m


if __name__ == "__main__":
    main()
