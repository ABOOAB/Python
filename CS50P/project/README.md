# Sudoku Solver

### Video Demo: [Demo Video](https://youtu.be/CedFm8YVoJI)

### Description:
Sudoku Solver is a Python application designed to assist users in solving Sudoku puzzles efficiently. Sudoku puzzles, a popular pastime for puzzle enthusiasts, require players to fill a 9x9 grid with digits while adhering to specific rules. This project aims to simplify the solving process by providing a user-friendly interface and robust solving algorithms.

#### Introduction:
Sudoku is a logic-based puzzle game that has gained immense popularity worldwide. The game consists of a 9x9 grid divided into nine 3x3 subgrids. The objective is to fill the grid with digits from 1 to 9, ensuring that each column, each row, and each of the nine 3x3 subgrids contains all the digits exactly once. While Sudoku puzzles can be solved manually, complex puzzles may require significant time and effort. Sudoku Solver offers a solution by automating the solving process, allowing users to solve puzzles with ease.

#### Files Overview:
##### project.py:
The project.py file serves as the main script for the Sudoku Solver application. It orchestrates the solving process by providing user prompts for input methods, validating the initial puzzle, solving the puzzle using backtracking algorithms, and displaying the solution to the user.

##### utilities.py:
The utilities.py file contains utility functions used by project.py. These functions handle tasks such as printing the Sudoku puzzle, confirming the puzzle with the user, loading an image for puzzle extraction, and extracting digits from puzzle squares in an image.

##### recognizer.py:
The recognizer.py file implements a class Recognizer that facilitates the extraction of digits from puzzle squares in an image. It utilizes OpenCV for image processing and a convolutional neural network model trained on the MNIST dataset to recognize digits.

##### test_project.py:
The test_project.py file contains unit tests for validating the functionality of the Sudoku solving algorithms and utility functions. It includes tests for functions such as is_valid_puzzle(), empty_square(), is_valid(), and solve_sudoku().

##### requirements.txt:
The requirements.txt file lists all the Python packages required by the project, ensuring consistent dependencies across different environments. It includes packages such as OpenCV, NumPy, and TensorFlow.

#### Design Choices:
##### Input Methods:
The project offers two input methods: keyboard input and image upload. This choice was made to cater to different user preferences and scenarios. While keyboard input provides a straightforward way for users to input puzzles manually, image upload leverages image processing techniques to extract puzzles from images, offering convenience and versatility.

##### Backtracking Algorithm:
The decision to use a backtracking algorithm for solving Sudoku puzzles was based on its efficiency and effectiveness. Backtracking is a systematic approach that explores all possible solutions recursively, efficiently navigating through the puzzle's solution space to identify the correct arrangement of numbers. This algorithm ensures that all valid solutions are explored while minimizing unnecessary computations.

##### Unit Testing:
The inclusion of unit tests in test_project.py ensures the reliability and correctness of the Sudoku solving algorithms and utility functions. By systematically testing individual components of the codebase, we can identify and fix issues early in the development process, maintaining code quality and facilitating future enhancements.

#### Conclusion:
Sudoku Solver is a versatile and efficient tool for solving Sudoku puzzles, offering users a seamless solving experience through intuitive input methods and robust solving algorithms. By leveraging keyboard input and image processing techniques, the project caters to a wide range of user preferences and scenarios. With a focus on reliability, efficiency, and user-friendliness, Sudoku Solver aims to provide Sudoku enthusiasts with a satisfying solving experience.

