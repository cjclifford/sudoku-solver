def nextEmptyCell(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

def isValid(grid, i, j, e):
    if all([e != grid[x][j] for x in range(9)]):
        if all([e != grid[i][y] for y in range(9)]):
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
        return False

def solveSudoku(grid, i = 0, j = 0):
    i, j = nextEmptyCell(grid)
    if i == -1:
        return True

    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
    grid[i][j] = 0
    return False

def printSudoku(grid):
    solveSudoku(grid)
    for row in grid:
        print(row)

test = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

printSudoku(test)
