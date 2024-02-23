s = input("camelCase: ")
for c in s:
    if c.islower() == True:
        print(f"{c}", end="")
    else:
        print(f"_{c.lower()}", end="")
print()
