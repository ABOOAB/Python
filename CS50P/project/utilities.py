from recognizer import Recognizer
import cv2
import numpy as np
import re
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.keras.models import load_model


# function to print the game
def print_game(cells):
    chunk_line = '\t\033[93m-------------------------------------\033[0m'
    line = '\t-------------------------------------'
    print("\n")
    # print the upper line
    print(chunk_line) # change the default color for the chunck borders
    for i in range(9):
        print("\t\033[93m|\033[0m", end='')
        for j in range(9):
            item = cells[i][j]
            if item == 0:
                item = ' '
            print(f' {item} |', end='') if (j + 1) % 3 else print(f' {item} \033[93m|\033[0m', end='')
        print('')
        print(line) if (i + 1) % 3 else print(chunk_line)
    print("\n")

def confirm(puzzle):
    confirm = 'no'
    while confirm != 'yes':
        print("Please confirm if this is your intended Sudoku board")
        print_game(puzzle)
        confirm = input("Is this correct? (yes or no): ").lower()
        if confirm not in ['yes', 'no']:
            print("Please Enter A Valid Answer")

    return True

# function to load image
def load_image():
    path = input("What is the path of your puzzle image? \nPlease provide a clear Sudoku puzzle with a visible outer border: ")
    image = cv2.imread(path)
    while image is None:
        path = input("Please enter a valid path")
        image = cv2.imread(path)
    return image

# function to extract digit from picture store it in a list
def use_image():
    puzzle = Recognizer()
    model = load_model('digit-classifier.h5')
    height = 450
    width = 450

    image = load_image()
    image = cv2.resize(image, (width, height))

    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgThresh = cv2.adaptiveThreshold(imgBlur, 255, 1, 1, 11, 2)

    # Find all the contours in the image
    imgContours = image.copy()
    imgLargestContours = image.copy()
    contours, _ = cv2.findContours(imgThresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)

    # Find the biggest contour in the image and use it as the Sudoku board
    biggest = puzzle.findBiggestContour(contours)
    try:
        if biggest.size != 0:	#if a board was found
            biggest = puzzle.reorderCorners(biggest)
            cv2.drawContours(imgLargestContours, biggest, -1, (0, 0, 255), 25)
            p1 = np.float32(biggest)
            p2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv2.getPerspectiveTransform(p1, p2)
            imgWarp = cv2.warpPerspective(image, matrix, (width, height))
            imgWarp = cv2.cvtColor(imgWarp, cv2.COLOR_BGR2GRAY)
    except:
        return None

    # Split the image into each square and determine the digit using prediction model
    squares = puzzle.getSquares(imgWarp)
    cells = puzzle.getDigit(squares, model)

    return cells if confirm(cells) else None


def use_keyboard():
    print("Please enter the puzzle squares. Use space for empty squares.")
    cells =  []
    for i in range(9):
        print(f"row {i + 1}")
        cells.append([])
        row = input()
        while not re.match(r'^[1-9 ]{9}$', row):
            row = input("Please enter the row again: ")
        for j in range(9):
            cells[i].append(int(row[j])) if row[j] != ' ' else cells[i].append(0)
    return cells if confirm(cells) else None

