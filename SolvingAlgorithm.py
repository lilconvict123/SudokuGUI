def find0():

    for row in range(9):
        for column in rnge(9):
            if board[row][column] == 0:
                return (row,column)
    return -1

def valid(board, num, pos):

    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(board):

    zeroCoord = find0()

    if zeroCoords == -1:
        return True

    row, column = zeroCoords
    for count in range(1,10):
        if valid(board,count,(row,column)):
            board[row][column] = count
            if solve(board):
                return True
            board[row][column] = 0 
    return False