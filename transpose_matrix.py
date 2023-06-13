# O(w * h) time | O(w * h) space - where w is the
# width of the matrix and h is the height
def transposeMatrix(matrix):
    # Write your code here.
    transposedMatrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)
    return transposedMatrix