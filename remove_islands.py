# O(wh) time | O(wh) space - where w and h
# are the width and height of the input matrix
def removeIslands(matrix):
    # Write your code here.
    # Find all the 1s that are not islands
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue

            changeOnesConnectedToBorderToTwos(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color = matrix[row][col]
            if color == 1:
                matrix[row][col] = 0
            elif color == 2:
                matrix[row][col] = 1
            
    return matrix


def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition

        matrix[currentRow][currentCol] = 2

        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[row])

    if row - 1 >= 0:   # UP
        neighbors.append((row - 1, col))
    if row + 1 < numRows:   # DOWN
        neighbors.append((row + 1, col))
    if col - 1 >= 0:   # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < numCols:   # RIGHT
        neighbors.append((row, col + 1))

    return neighbors



# Solution 2
# O(wh) time | O(wh) space - where w and h
# are the width and height of the input matrix
# def removeIslands(matrix):
#     # Write your code here.
#     onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]

#     # Find all the 1s that are not islands
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             rowIsBorder = row == 0 or row == len(matrix) - 1
#             colIsBorder = col == 0 or col == len(matrix[row]) - 1
#             isBorder = rowIsBorder or colIsBorder
#             if not isBorder:
#                 continue

#             if matrix[row][col] != 1:
#                 continue

#             findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

#     for row in range(1, len(matrix) - 1):
#         for col in range(1, len(matrix[row]) - 1):
#             if onesConnectedToBorder[row][col]:
#                 continue

#             matrix[row][col] = 0
            
#     return matrix


# def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
#     stack = [(startRow, startCol)]

#     while len(stack) > 0:
#         currentPosition = stack.pop()
#         currentRow, currentCol = currentPosition

#         alreadyVisited = onesConnectedToBorder[currentRow][currentCol]
#         if alreadyVisited:
#             continue

#         onesConnectedToBorder[currentRow][currentCol] = True

#         neighbors = getNeighbors(matrix, currentRow, currentCol)
#         for neighbor in neighbors:
#             row, col = neighbor

#             if matrix[row][col] != 1:
#                 continue

#             stack.append(neighbor)


# def getNeighbors(matrix, row, col):
#     neighbors = []

#     numRows = len(matrix)
#     numCols = len(matrix[row])

#     if row - 1 >= 0:   # UP
#         neighbors.append((row - 1, col))
#     if row + 1 < numRows:   # DOWN
#         neighbors.append((row + 1, col))
#     if col - 1 >= 0:   # LEFT
#         neighbors.append((row, col - 1))
#     if col + 1 < numCols:   # RIGHT
#         neighbors.append((row, col + 1))

#     return neighbors
