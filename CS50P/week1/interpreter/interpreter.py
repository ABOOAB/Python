def main():
    x, y, z = input("Expresion : ").strip().split(" ")
    match y:
        case "+":
            sum(x, z)
        case "-":
            sub(x, z)
        case "*":
            mul(x, z)
        case "/":
            div(x, z)


def sum(a, b):
    print(float(a) + float(b))


def sub(a, b):
    print(float(a) - float(b))


def mul(a, b):
    print(float(a) * float(b))


def div(a, b):
    print(float(a) / float(b))


main()
