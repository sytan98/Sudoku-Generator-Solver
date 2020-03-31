def backtrack(sudokuobj):
    #base cases
    if sudokuobj.check_grid():
        print("solved")
        return True
    #horizontal wise needs to be unique
    for idx, i in enumerate(sudokuobj.flatlist):
        if i == 0:
            for j in range(1,10):
                row = idx//9
                column = idx%9
                subsquare = (idx//9//3)*3+(idx%9//3+1)-1
                # print(idx, row, column, subsquare, j)
                if (sudokuobj.check_inrow(row, j) and sudokuobj.check_incolumn(column, j) and sudokuobj.check_insubsquare(subsquare,j)):
                    # print("found an element that might be suitable")
                    sudokuobj.list[row][column] = j
                    # print(sudokuobj.rows)
                    
                    # print("trying for next empty element")
                    if backtrack(sudokuobj):
                        return True
                    
                    
            break
    # print("Previous element not suitable, backtracking..")
    sudokuobj.list[idx//9][idx%9] = 0
    return False