

def main():
    text = input("greetin: ")
    print(f"${value(text)}")


def value(greeting):
    greeting = greeting.lower()
    if greeting.split()[0] == "hello" or greeting.split()[0] == "hello,":
        return 0

    elif greeting[0] == "h":
        return 20
    else:
        return 100




if __name__ == "__main__" :
    main()