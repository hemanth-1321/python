def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    
    # Check upper diagonal on the right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
        if board[i] == j:
            return False
    
    return True

def solve_queens_util(board, row):
    if row >= 8:
        # All queens are placed
        return True
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens_util(board, row + 1):
                # If placing queen in board[row][col] doesn't lead to a solution, backtrack
                return True
            board[row] = -1
    
    return False

def solve_queens():
    board = [-1] * 8  # Initialize board with -1 indicating no queen placed in that row
    if not solve_queens_util(board, 0):
        print("Solution does not exist")
        return False
    
    print("Solution:")
    for i in range(8):
        for j in range(8):
            if board[i] == j:
                print("Q", end="")
            else:
                print(".", end="")
        print()
    
    return True

# Main Program
solve_queens()