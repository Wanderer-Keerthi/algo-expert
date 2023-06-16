# Upper Bound: O(n!) time | O(n) space - where n is the input number
def nonAttackingQueens(n):
    # Write your code here.
    blockedColumns = set()
    blockedUpDiagonals = set()
    blockedDownDiagonals = set()
    return getNumberOfNonAttackingQueenPlacements(0, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, n)


def getNumberOfNonAttackingQueenPlacements(row, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize):
    if row == boardSize:
        return 1

    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
            placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
            validPlacements += getNumberOfNonAttackingQueenPlacements(
                row + 1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize
            )
            removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)

    return validPlacements


# This is always an O(1)-time operation.
def isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    if col in blockedColumns:
        return False
    if row + col in blockedUpDiagonals:
        return False
    if row - col in blockedDownDiagonals:
        return False

    return True


def placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.add(col)
    blockedUpDiagonals.add(row + col)
    blockedDownDiagonals.add(row - col)


def removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.remove(col)
    blockedUpDiagonals.remove(row + col)
    blockedDownDiagonals.remove(row - col)



# Solution 2
# Lower Bound: O(n!) time | O(n) space - where n is the input number
# def nonAttackingQueens(n):
#     # Write your code here.
#     # Each index of `columnPlacements` represents a row of the chessboard,
#     # and the value at each index is the column (on the relevant row) where
#     # a queen is currently placed.
#     columnPlacements = [0] * n
#     return getNumberOfNonAttackingQueenPlacements(0, columnPlacements, n)


# def getNumberOfNonAttackingQueenPlacements(row, columnPlacements, boardSize):
#     if row == boardSize:
#         return 1

#     validPlacements = 0
#     for col in range(boardSize):
#         if isNonAttackingPlacement(row, col, columnPlacements):
#             columnPlacements[row] = col
#             validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, columnPlacements, boardSize)

#     return validPlacements


# # As `row` tends to `n`, this becomes an O(n)-time operation.
# def isNonAttackingPlacement(row, col, columnPlacements):
#     for previousRow in range(row):
#         columnToCheck = columnPlacements[previousRow]
#         sameColumn = columnToCheck == col
#         onDiagonal = abs(columnToCheck - col) == row - previousRow
#         if sameColumn or onDiagonal:
#             return False

#     return True
