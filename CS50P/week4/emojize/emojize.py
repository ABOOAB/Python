import emoji


s = input("Input: ")
output = emoji.emojize(s,language='alias')
print(f"Output: ", output)
