
import cv2
import numpy as np

class Recognizer:
    # Find the biggest contour by area and return its four corners and area
    def __init__(self):
        pass

    def findBiggestContour(self, contours):
        self.biggest_contour = []
        self.max_area = 0
        for c in contours:
            area = cv2.contourArea(c)
            if area > 50:
                perim = cv2.arcLength(c, True)
                corners = cv2.approxPolyDP(c, 0.02 * perim, True)
                if area > self.max_area and len(corners) == 4:
                    self.biggest_contour = corners
                    self.max_area = area

        return self.biggest_contour

    # Re-order the corners of the biggest contour as ([0,0], [0, width], [height, 0], [height, width])
    def reorderCorners(self, corners):
        corners = corners.reshape((4,2))
        self.ordered = np.zeros((4, 1, 2), dtype = int)
        total = corners.sum(1)
        self.ordered[0] = corners[np.argmin(total)]  #smallest sum of points is origin
        self.ordered[3] = corners[np.argmax(total)]  #largest sum of points is last
        diff = np.diff(corners, axis=1)
        self.ordered[1] = corners[np.argmin(diff)]   #negative difference in points is second
        self.ordered[2] = corners[np.argmax(diff)]   #positive difference in points is third
        return self.ordered

    # Split the Sudoku board into each individual square
    def getSquares(self, board):
        self.rows = np.vsplit(board, 9)
        self.squares = []
        for row in self.rows:
            cols = np.hsplit(row, 9)
            for square in cols:
                self.squares.append(square)

        return self.squares


    # Determine the digit in the square using prediction model
    def getDigit(self, squares, model):
        self.numbers = []
        for sq in squares:
            img = np.asarray(sq)
            img = img[6:img.shape[0] - 6, 6:img.shape[1] - 6]
            img = cv2.resize(img, (28,28))
            img = img / 255
            img = img.reshape(1, 28, 28, 1)
            prediction = model.predict(img, verbose=0)
            index = np.argmax(prediction, axis=-1)
            prob = np.amax(prediction)
            if prob > 0.8:
                self.numbers.append(index[0])
            else:
                self.numbers.append(0)
        self.numbers = [self.numbers[i:i+9] for i in range(0, 81, 9)]
        return self.numbers

