import random
import copy
from Solver import *
from sudoku import *

def generator(sudokuobj):
    #base cases
    if sudokuobj.check_grid():
        print("solved")
        return True
    #horizontal wise needs to be unique
    for idx, i in enumerate(sudokuobj.flatlist):
        if i == 0:
            numbers = [x for x in range(9)]
            random.shuffle(numbers)
            for j in numbers:
                row = idx//9
                column = idx%9
                subsquare = (idx//9//3)*3+(idx%9//3+1)-1
                print(idx, row, column, subsquare, j)
                if (sudokuobj.check_inrow(row, j) and sudokuobj.check_incolumn(column, j) and sudokuobj.check_insubsquare(subsquare,j)):
                    print("found an element that might be suitable")
                    sudokuobj.list[row][column] = j
                    
                    print("trying for next empty element")
                    if backtrack(sudokuobj):
                        return True
            break
    print("Previous element not suitable, backtracking..")
    sudokuobj.list[idx//9][idx%9] = 0
    return False

def question(difficulty):
    if difficulty == "easy":
        n = 40
    elif difficulty == "medium":
        n = 50
    else:
        n = 60
    emptygrid = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

    question = sudoku(emptygrid)
    generator(question)

    idx = [x for x in range(81)]

    for i in range(n):
        random_idx = random.choice(idx)
        idx.remove(random_idx)
        row = random_idx//9
        column = random_idx%9
        backup = question.list[row][column]
        question.list[row][column] = 0
        # counter =  0
        copysudoku = copy.deepcopy(question)
        if not (backtrack(copysudoku)):        
            print("some error")
            question.list[row][column] = backup
    return question
