import inflect

p = inflect.engine()
my_list = []
while True:
    try:
        s = input("Input: ")
        my_list.append(s)

    # for i in range(len(sys.argv[1:])):
    #     my_list = my_list.append(sys.argv[i])
    except EOFError:
        break
my_list = p.join(my_list)
print("Adieu, adieu, to", my_list)
# print(my_list
# mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot
