
# solve the eight queen problem



def eight_queens(size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    solutions = []

    def is_valid(row, col):
        # check column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # check diagonal left up
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False

            i -= 1
            j -= 1

        # check diagonal right up 
        i, j = row, col 
        while i >= 0 and j < size: 
            if board[i][j] == 1: 
                return False

            i -= 1 
            j += 1

        return True

    def solve(row): 
        if row == size:  # all queens are placed successfully 
            solutions.append([list(x) for x in board])  # add solution to list of solutions  

            return True   # done!  

        for col in range(size):   # try all columns of current row  

            if is_valid(row, col):   # check if it's valid to place a queen at (row, col)  

                board[row][col] = 1   # place the queen at (row, col)  

                solve(row + 1)   # solve the rest of the problem recursively. Note that we don't have to worry about undoing our changes here because we are working with a copy of the original board.  

                board[row][col] = 0   # un-place the queen at (row, col) so that we can try other columns on this row. Again, no need to worry about undoing our changes because we are working with a copy of the original board.  

    solve(0)  # start solving from row 0   

    return solutions