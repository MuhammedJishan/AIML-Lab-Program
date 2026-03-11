# 8 Queen Problem
# Recursive solution

import time

numQueens = 8  # number of queens

currentSolution = [0 for x in range(numQueens)]
solutions = []


def isSafe(testRow, testCol):
    # no need to check for row 0
    if testRow == 0:
        return True

    for row in range(0, testRow):
        # check vertical
        if testCol == currentSolution[row]:
            return False

        # check diagonal
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False

    return True


def placeQueen(row):
    global currentSolution, solutions, numQueens

    for col in range(numQueens):
        if not isSafe(row, col):
            continue
        else:
            currentSolution[row] = col

            if row == (numQueens - 1):
                # last row
                solutions.append(currentSolution.copy())
            else:
                placeQueen(row + 1)


# start solving
placeQueen(0)

print(len(solutions), "solutions found")
for solution in solutions:
    print(solution)
