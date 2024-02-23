import random

while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            raise ValueError

    except ValueError:
        pass

    else:
        break

num = random.randint(1, n)
while True:
    try:
        s = int(input("Guess: "))
        if s > num:
            print("Too large!")
            raise ValueError
        elif s < num:
            print("Too small!")
            raise ValueError

    except ValueError:
        pass
    else:
        break

print("Just right!")

