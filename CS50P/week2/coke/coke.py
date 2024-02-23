due = 50
while True:
    print(f"Amount Due: {due}")
    ins = int(input("Insert coin: "))
    if ins in [5, 10, 25]:
        due = due - ins
        if due <= 0:
            break

print(f"Change Owed: {due * (-1)}")
