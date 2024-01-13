 # A dictionary of available items
available_items = {
    "Google Pixel 6a": {"price": 280, "quantity": 5},
    "SAMSUNG Galaxy S23 Ultra": {"price": 1200, "quantity": 3},
    "iPhone 13 Pro Max": {"price": 1300, "quantity": 2},
    "Xiaomi Redmi 9A": {"price": 100, "quantity": 4},
    "Huawei P50 Pro": {"price": 1000, "quantity": 1},
    "OnePlus 9 Pro": {"price": 800, "quantity": 1},
}

cart = {}
menu_message = '''
what would you like to do?
1. view items and buy
2. view cart
3. view total price in cart
4. exit the program
'''
while True:
    print(menu_message)

    #get the user choice
    choice = input('Enter the number of your choice: ')
    if choice == '1':

        # view all items
        for i, item in enumerate(available_items):
            if available_items[item]['quantity'] != 0:
                print(f"{i + 1}. {item}: $ {available_items[item]['price']}")
            else:
                print(f"{i + 1}. {item}: $ {available_items[item]['price']} (out of stock)")
        
        #get purchaced item
        item_number = int(input("Enter a number of item you want to buy or 0 to return: "))
        if item_number == 0:
            continue
        order_name = list(available_items.keys())[item_number - 1]

        # check if the item out of stock
        if available_items[order_name]['quantity'] :
            order_price = available_items[order_name]['price']
            order_quantitiy = cart.get(order_name, {}).get('quantity', 0) + 1
            available_items[order_name]['quantity'] -= 1
        else:
            print("Sorry cant't add item, the item out of stock")
            continue

        # add order infor to cart
        order_info = {
            order_name :{
                'price': order_price ,
                'quantity' : order_quantitiy
            }
        }
        cart.update(order_info )

    # view cart 
    elif choice == '2':
        if cart: 
            total_price = sum([cart[item]['price'] * cart[item]['quantity'] for item in cart])
            for item in cart:
                print(f"{item}: {cart[item]['price']} x {cart[item]['quantity']}")
            print(f"The total cost in cart is : {total_price}")

        else:
            print('Cart is empty.')


    # view total price in cart
    elif choice == '3':
        if cart:
            total_price = sum([cart[item]['price'] * cart[item]['quantity'] for item in cart])
            # for item in cart:
            #     total_price += cart[item]['price'] * cart[item]['quantity']
            print(f"The total cost in cart is : {total_price}")
        else :
            print('The cart is empty')


    
    elif choice == '4':
        print('exiting the program........', end='\n\n')
        break

    # invalid input case
    else:
        print('Enter a valid choice')
        continue

if cart: 
    total_price = sum([cart[item]['price'] * cart[item]['quantity'] for item in cart])
    for item in cart:
        print(f"{item}: {cart[item]['price']} x {cart[item]['quantity']}")
    print(f"The total cost in cart is : {total_price}")

else:
    print('Cart is empty.')

