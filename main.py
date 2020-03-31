from sudoku import *
from Solver import *
from Generator import *

counter = 0
test = [[0, 0, 0, 0, 5, 0, 7, 0, 9],
        [0, 5, 6, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 1, 0, 4, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 7],
        [5, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 8, 0, 3, 7, 0, 1, 0],
        [0, 0, 5, 0, 0, 8, 0, 0, 0],
        [8, 6, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 2, 6, 0, 0]]

def main():
    sample1 = question("hard")
    print(sample1.rows)
    backtrack(sample1)
    print(sample1.rows)
if __name__ == "__main__":
    main()