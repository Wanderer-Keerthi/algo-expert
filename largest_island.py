# O(w * h) time | O(w * h) space - where w is the width of the matrix, and
# h is the height of the matrix
def largestIsland(matrix):
    # Write your code here.
    islandSizes = []
    # islandNumber starts at 2 to avoid overwriting existing 0s and 1s
    islandNumber = 2
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1:
                islandSizes.append(getSizeFromNode(row, col, matrix, islandNumber))
                islandNumber += 1

    maxSize = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                continue

            landNeighbors = getLandNeighbors(row, col, matrix)
            islands = set()
            for neighbor in landNeighbors:
                islands.add(matrix[neighbor[0]][neighbor[1]])

            size = 1
            for island in islands:
                size += islandSizes[island - 2]
            maxSize = max(maxSize, size)

    return maxSize


def getSizeFromNode(row, col, matrix, islandNumber):
    size = 0
    nodesToExplore = [[row, col]]
    while len(nodesToExplore) > 0:
        currentNode = nodesToExplore.pop()
        currentRow, currentCol = currentNode[0], currentNode[1]

        if matrix[currentRow][currentCol] != 0:
            continue

        matrix[currentRow][currentCol] = islandNumber
        size += 1
        nodesToExplore += getLandNeighbors(currentRow, currentCol, matrix)

    return size


def getLandNeighbors(row, col, matrix):
    landNeighbors = []
    if row > 0 and matrix[row - 1][col] != 1:
        landNeighbors.append([row - 1, col])
    if row < len(matrix) - 1 and matrix[row + 1][col] != 1:
        landNeighbors.append([row + 1, col])
    if col > 0 and matrix[row][col - 1] != 1:
        landNeighbors.append([row, col - 1])
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] != 1:
        landNeighbors.append([row, col + 1])

    return landNeighbors



# Solution 2
# O(w^2 * h^2) time | O(w * h) space - where w is the width of the matrix, and
# h is the height of the matrix
# def largestIsland(matrix):
#     # Write your code here.
#     maxSize = 0
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if matrix[row][col] == 0:
#                 continue

#             maxSize = max(maxSize, getSizeFromNode(row, col, matrix))
            
#     return maxSize


# def getSizeFromNode(row, col, matrix):
#     size = 1
#     visited = [[False for value in row] for row in matrix]
#     nodesToExplore = getLandNeighbors(row, col, matrix)
#     while len(nodesToExplore) > 0:
#         currentNode = nodesToExplore.pop()
#         currentRow, currentCol = currentNode[0], currentNode[1]

#         if visited[currentRow][currentCol]:
#             continue

#         visited[currentRow][currentCol] = True
#         size += 1
#         nodesToExplore += getLandNeighbors(currentRow, currentCol, matrix)

#     return size


# def getLandNeighbors(row, col, matrix):
#     landNeighbors = []
#     if row > 0 and matrix[row - 1][col] != 1:
#         landNeighbors.append([row - 1, col])
#     if row < len(matrix) - 1 and matrix[row + 1][col] != 1:
#         landNeighbors.append([row + 1, col])
#     if col > 0 and matrix[row][col - 1] != 1:
#         landNeighbors.append([row, col - 1])
#     if col < len(matrix[0]) - 1 and matrix[row][col + 1] != 1:
#         landNeighbors.append([row, col + 1])

#     return landNeighbors
