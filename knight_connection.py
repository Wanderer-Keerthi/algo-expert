import math

# O(n * m) time | O(n * m) space - where n is horizantal distance between
# the knights and m is the vertical distance between the knights
def knightConnection(knightA, knightB):
    # Write your code here.
    possibleMoves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    queue = [[knightA[0], knightA[1], 0]]
    visited = {positionToString(knightA)}

    while True:
        # In Python, popping elements from the start of a list is an O(n)-time operation.
        # To make this an O(1)-time operation, we could use the `deque` object.
        # For our time complexity analysis, we'll assume this runs in O(1) time
        currentPosition = queue.pop(0)

        if currentPosition[0] == knightB[0] and currentPosition[1] == knightB[1]:
            return math.ceil(currentPosition[2] / 2)

        for possibleMove in possibleMoves:
            position = [currentPosition[0] + possibleMove[0], currentPosition[1] + possibleMove[1]]
            positionString = positionToString(position)
            if positionString not in visited:
                position.append(currentPosition[2] + 1)
                queue.append(position)
                visited.add(positionString)

def positionToString(position):
    return ",".join(map(str, position))      