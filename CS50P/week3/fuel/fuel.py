while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        if int(x) > int(y):
            raise ValueError

        result = int(round(int(x) / int(y) * 100))

    except (ValueError, ZeroDivisionError):
        pass

    else:
        break
# convert the value to precent
if result >= 99:
    print("F")
elif result <= 1:
    print("E")
else:
    print(f"{result}%")
