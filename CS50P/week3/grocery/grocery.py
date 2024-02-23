d = {}

while True:
    try:
        item = input().lower()
        if item in d:
            d[item] += 1
        else:
            raise KeyError

    except KeyError:
        d[item] = 1
    except EOFError:
        break

s = sorted(d.keys())
for item in s:
    print(f"{d[item]} {item.upper()}")
