s = input("Input: ")
for c in s:
    if c.lower() in ["a", "e", "i", "u", "o"]:
        continue
    else:
        print(c, end="")
print()
