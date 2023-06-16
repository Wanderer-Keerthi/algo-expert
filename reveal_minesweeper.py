# O(w * h) time | O(w * h) space - where w is the width of the board, and
# h is the height of the board
def revealMinesweeper(board, row, column):
    # Write your code here.
    if board[row][column] == "M":
        board[row][column] = "X"
        return board

    neighbors = getNeighbors(board, row, column)
    adjacentMinesCount = 0
    for neighborRow, neighborColumn in neighbors:
        if board[neighborRow][neighborColumn] == "M":
            adjacentMinesCount += 1

    if adjacentMinesCount > 0:
        board[row][column] = str(adjacentMinesCount)
    else:
        board[row][column] = "0"
        for neighborRow, neighborColumn in neighbors:
            if board[neighborRow][neighborColumn] == "H":
                revealMinesweeper(board, neighborRow, neighborColumn)
                
    return board


def getNeighbors(board, row, column):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []
    for directionRow, directionColumn in directions:
        newRow = row + directionRow
        newColumn = column + directionColumn
        if 0 <= newRow < len(board) and 0 <= newColumn < len(board[0]):
            neighbors.append([newRow, newColumn])

    return neighbors
