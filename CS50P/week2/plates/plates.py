def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #  vanity plates may contain a maximum of 6 characters
    # (letters or numbers) and a minimum of 2 characters.
    if len(s) > 6 or len(s) < 2:
        return False
    # No periods, spaces, or punctuation marks are allowed.
    for c in s:
        if c.isalpha() == False and c.isdigit() == False:
            return False

    #  All vanity plates must start with at least two letters.
    if s[0:2].isalpha() == False:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    #  For example, AAA222 would be an acceptable … vanity plate; AAA22A would
    #  not be acceptable. The first number used cannot be a ‘0’
    if s.isalpha() == False:
        for c in s[2:]:
            if c.isalpha() == True:
                continue
            else:
                if c == "0":
                    return False
                else:
                    break
    for c in range(len(s) - 1):
        if s[c].isdigit() == True and s[c + 1].isalpha() == True:
            return False

    return True


main()
