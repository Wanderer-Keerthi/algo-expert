# O(w * h) time | O(w * h) space - where w is the
# width of the matrix and h is the height
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else -1


def convertNegatives(matrix):
    queue = getAllPositivePositions(matrix)

    passes = 0

    while len(queue) > 0:
        currentSize = len(queue)

        while currentSize > 0:
            # In Python, popping elements from the start of a list is an O(n)-time operation.
            # To make this an O(1)-time operation, we could use the `deque` object.
            # For our time complexity analysis, we'll assume this runs in O(1) time.
            currentRow, currentCol = queue.pop(0)

            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position

                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    queue.append([row, col])

            currentSize -= 1

        passes += 1

    return passes


def getAllPositivePositions(matrix):
    positivePositions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positivePositions.append([row, col])

    return positivePositions


def getAdjacentPositions(row, col, matrix):
    adjacentPositions = []

    if row > 0:
        adjacentPositions.append([row - 1, col])
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])
    if col > 0:
        adjacentPositions.append([row, col - 1])
    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])

    return adjacentPositions


def containsNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True

    return False



# Solution 1
# O(w * h) time | O(w * h) space - where w is the
# width of the matrix and h is the height
# def minimumPassesOfMatrix(matrix):
#     # Write your code here.
#     passes = convertNegatives(matrix)
#     return passes - 1 if not containsNegative(matrix) else -1


# def convertNegatives(matrix):
#     nextPassQueue = getAllPositivePositions(matrix)

#     passes = 0

#     while len(nextPassQueue) > 0:
#         currentPassQueue = nextPassQueue
#         nextPassQueue = []

#         while len(currentPassQueue) > 0:
#             # In Python, popping elements from the start of a list is an O(n)-time operation.
#             # To make this an O(1)-time operation, we could use the `deque` object.
#             # For our time complexity analysis, we'll assume this runs in O(1) time.
#             # Also, for this particular solution (Solution #1), we could actually
#             # just turn this queue into a stack and replace `.pop(0)` with the
#             # constant-time `.pop()` operation.
#             currentRow, currentCol = currentPassQueue.pop(0)

#             adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
#             for position in adjacentPositions:
#                 row, col = position

#                 value = matrix[row][col]
#                 if value < 0:
#                     matrix[row][col] *= -1
#                     nextPassQueue.append([row, col])

#         passes += 1

#     return passes


# def getAllPositivePositions(matrix):
#     positivePositions = []

#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             value = matrix[row][col]
#             if value > 0:
#                 positivePositions.append([row, col])

#     return positivePositions


# def getAdjacentPositions(row, col, matrix):
#     adjacentPositions = []

#     if row > 0:
#         adjacentPositions.append([row - 1, col])
#     if row < len(matrix) - 1:
#         adjacentPositions.append([row + 1, col])
#     if col > 0:
#         adjacentPositions.append([row, col - 1])
#     if col < len(matrix[0]) - 1:
#         adjacentPositions.append([row, col + 1])

#     return adjacentPositions


# def containsNegative(matrix):
#     for row in matrix:
#         for value in row:
#             if value < 0:
#                 return True

#     return False
