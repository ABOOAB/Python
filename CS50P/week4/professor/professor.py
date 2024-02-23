
import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        chances = 0
        a = generate_integer(level)
        b = generate_integer(level)
        # print(f'{a} + {b} = ', '')
        while True:
            try:
                ans = int(input(f"{a} + {b} = "))
                if ans != a + b:
                    raise ValueError
                else:
                    score += 1
                    break

            except ValueError:
                chances += 1

                print("EEE")
                if chances != 3:
                    pass
                else:
                    print(f"{a} + {b} = {a + b}")
                    break
    print(f"score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in (1, 2, 3):
                return n

        except ValueError:
            pass

    ...


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

    else:
        raise ValueError

    ...


if __name__ == "__main__":
    main()
