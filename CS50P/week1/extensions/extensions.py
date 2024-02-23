def main():
    s = input("File name: ")
    s = ext(s.lower())

    match s:
        case "gif" | "jpeg" | "png":
            print(f"image/{s}")
        case "zip" | "pdf":
            print(f"application/{s}")
        case "plain":
            print(f"text/{s}")
        case _:
            print("application/octet-stream")


def ext(t):
    if ".gif" in t:
        return "gif"
    elif ".jpeg" in t or ".jpg" in t:
        return "jpeg"
    # elif ".jpg" in t:
    #     return "jpeg"
    elif ".zip" in t:
        return "zip"
    elif ".pdf" in t:
        return "pdf"
    elif ".txt" in t:
        return "plain"
    elif ".png" in t:
        return "png"
    else:
        return "another"


main()
