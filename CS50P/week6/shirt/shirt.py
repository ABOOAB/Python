import sys
from PIL import Image, ImageOps
import os


def main():
    # check the number of arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # check the extention of the files
    ext = [".jpg", ".jpeg", ".png"]
    inp= os.path.splitext(sys.argv[1])
    outp = os.path.splitext(sys.argv[2])
    if inp[1].lower() not in ext or outp[1].lower() not in ext:
        sys.exit("Invalid input")

    # check the similarity of input and output extintions
    if inp[1].lower() != outp[1].lower():
        sys.exit("Input and output have different extensions")

    # resizing and cropping the input
    # open the shirt file to resize and fit it
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as img:
            new_img = ImageOps.fit(img, shirt.size)
            new_img.paste(shirt, shirt)
            new_img.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input not found")


# overlay shirt.png (which has a transparent background) on the input

#  saving the result as its output


if __name__ == "__main__":
    main()
