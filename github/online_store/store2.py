# A dictionary of available items
available_items = {
    "Google Pixel 6a": {"price": 280, "quantity": 5},
    "SAMSUNG Galaxy S23 Ultra": {"price": 1200, "quantity": 3},
    "iPhone 13 Pro Max": {"price": 1300, "quantity": 2},
    "Xiaomi Redmi 9A": {"price": 100, "quantity": 4},
    "Huawei P50 Pro": {"price": 1000, "quantity": 1},
    "OnePlus 9 Pro": {"price": 800, "quantity": 1},
}

menu_message = """
what would you like to do?
1. view items and buy
2. view cart
3. view total price in cart
4. exit the program
"""

cart = {}


def main():
    while True:
        print(menu_message)
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                item = view_buy_items()
                if item:
                    buy(item - 1)
            case "2":
                view_cart()

            case "3":
                calculate_total()
            case "4":
                exit_program()
                break
            case _:
                print("Kindly Enter a valid choice")


def view_buy_items():
    for i, item in enumerate(available_items):
        print(f"{i + 1}. {item}: {available_items[item]['price']}")
    print("=" * 50)
    return int(input("Choice your item or Press (0) to back to the main menu: "))


def buy(item_num):
    item = list(available_items)[item_num]
    if 0 <= item_num < len(item):
        if available_items[item]["quantity"]:
            print(f"({item}) has been added to cart successfully😊")
            available_items[item]["quantity"] -= 1
            cart[item] = cart.get(item, 0) + 1 
        else:
            print(f"{item} out of stock 😥😣")
    else:
        print("Invalid item number. Please select a valid item.")

def view_cart():
    print('-'*50)
    for i, item in enumerate(cart):
        print(f"{i + 1}. {item} X {cart[item]}")
    
    

def calculate_total():
    print('Total price: ', end='')
    print(f"$ {sum([cart[item] * available_items[item]['price'] for item in cart])}") if cart else print('$ 0')


def exit_program():
    print('YOUR CART: ', end = '\n')
    view_cart();calculate_total() if cart else print( "Your cart is empty!")
    calculate_total()
    print("exittin ....", end="\n")
    print("")


if __name__ == "__main__":
    main()
