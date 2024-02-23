# cteate a dictionary of items and calries
# this version using list of dict
fruits = [
    {"Item": "Apple", "calories": "130"},
    {"Item": "Avocado", "calories": "50"},
    {"Item": "Banana", "calories": "110"},
    {"Item": "Cantaloupe", "calories": "50"},
    {"Item": "Grapefruit", "calories": "60"},
    {"Item": "Grapes", "calories": "90"},
    {"Item": "HoneydewMelon", "calories": "50"},
    {"Item": "Kiwifruit", "calories": "90"},
    {"Item": "Lemon", "calories": "15"},
    {"Item": "Lime", "calories": "20"},
    {"Item": "Nectarine", "calories": "60"},
    {"Item": "Orange", "calories": "80"},
    {"Item": "Peach", "calories": "60"},
    {"Item": "Pear", "calories": "100"},
    {"Item": "Pineapple", "calories": "50"},
    {"Item": "Plums", "calories": "70"},
    {"Item": "Strawberries", "calories": "50"},
    {"Item": "Sweet Cherries", "calories": "100"},
    {"Item": "Tangerine", "calories": "50"},
    {"Item": "Watermelon", "calories": "80"},
]
# prompt user to enter an item
s = input("Item: ").lower()
for fruit in fruits:
    if s == fruit["Item"].lower():
        print(fruit["calories"])

# this version using dict only


# fruits = {
#     "Apple": "130",
#     "Avocado": "50",
#     "Banana": "110",
#     "Cantaloupe": "50",
#     "Grapefruit": "60",
#     "Grapes": "90",
#     "HoneydewMelon": "50",
#     "Kiwifruit": "90",
#     "Lemon": "15",
#     "Lime": "20",
#     "Nectarine": "60",
#     "Orange": "80",
#     "Peach": "60",
#     "Pear": "100",
#     "Pineapple": "50",
#     "Plums": "70",
#     "Strawberries": "50",
#     "Sweet Cherries": "100",
#     "Tangerine": "50",
#     "Watermelon": "80",
# }
# # prompt user to enter an item
# s = input("Item: ").title()
# if s in fruits :
#     print(fruits[s])
