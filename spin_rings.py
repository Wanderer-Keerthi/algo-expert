# O(n) time | O(1) space - where n is the total number of elements in the array
def spinRings(array):
    # Write your code here.
    startRow, endRow = 0, len(array) - 1, 
    startCol, endCol = 0, len(array) - 1


    while startRow < endRow and startCol < endCol:
        originalTopRightValue = array[startRow][endCol]
    
        for col in reversed(range(startCol + 1, endCol + 1)):
            array[startRow][col] = array[startRow][col - 1]
    
        for row in range(startRow, endRow):
            array[row][startCol] = array[row + 1][startCol]
    
        for col in range(startCol, endCol):
            array[endRow][col] = array[endRow][col + 1]
    
        for row in reversed(range(startRow + 2, endRow + 1)):
            array[row][endCol] = array[row - 1][endCol]
    
        array[startRow + 1][endCol] = originalTopRightValue

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1    



# This question is equivalent to the Spiral Traverse question on AlgoExpert; we recommend watching the video explanation of that question to better understand this question's solution.

# The main differences here are that:

# 1) We're dealing only with square-shaped matrices, which simplifies the problem; we don't need to handle edge cases where we have a lone row or column in the middle of the matrix.
# 2) We're overwriting values in the input matrix, which means that we need to store a reference to one value in each spiral or ring that we spin--the top right value in our solutions--so as not to lose it forever in the process of spinning values.
# Otherwise, once again, this problem is equivalent to Spiral Traverse and can be implemented either recursively or iteratively; the iterative version is naturally better from a space-complexity point of view.

#  Complexity Analysis

# This question is self-evidently solved in linear time (with respect to the total number of value in the input matrix) and with constant space (for the iterative solution).

#  Closing Thoughts

# As mentioned a couple of times above, this question is a variant of the Spiral Traverse question on AlgoExpert. It's important to walk through an example with a large-enough matrix (a 5x5 matrix, for example) and to avoid off-by-one errors as we spin each ring with our for loops.




# Solution 2
# O(n) time | O(w) space - where n is the total number of
# elements in the array and w is the width of the array
# def spinRings(array):
#     # Write your code here.
#     spinRingsHelper(array, 0, len(array) - 1, 0, len(array) - 1)


# def spinRingsHelper(array, startRow, endRow, startCol, endCol):
#     if startRow >= endRow or startCol >= endCol:
#         return

#     originalTopRightValue = array[startRow][endCol]

#     for col in reversed(range(startCol + 1, endCol + 1)):
#         array[startRow][col] = array[startRow][col - 1]

#     for row in range(startRow, endRow):
#         array[row][startCol] = array[row + 1][startCol]

#     for col in range(startCol, endCol):
#         array[endRow][col] = array[endRow][col + 1]

#     for row in reversed(range(startRow + 2, endRow + 1)):
#         array[row][endCol] = array[row - 1][endCol]

#     array[startRow + 1][endCol] = originalTopRightValue

#     spinRingsHelper(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1)    




# def spinRings(array):
#     # Write your code here.
#     if not array:
#         return array

#     n = len(array)
#     start_row, start_col = 0, 0
#     end_row, end_col = n - 1, n - 1

#     while start_row < end_row and start_col < end_col:
#         # Store the first element of the current ring
#         prev = array[start_row + 1][start_col]

#         # Rotate the top row
#         for i in range(start_col, end_col + 1):
#             current = array[start_row][i]
#             array[start_row][i] = prev
#             prev = current

#         start_row += 1

#         # Rotate the right column
#         for i in range(start_row, end_row + 1):
#             current = array[i][end_col]
#             array[i][end_col] = prev
#             prev = current

#         end_col -= 1

#         # Rotate the bottom row
#         for i in range(end_col, start_col - 1, -1):
#             current = array[end_row][i]
#             array[end_row][i] = prev
#             prev = current

#         end_row -= 1

#         # Rotate the left column
#         for i in range(end_row, start_row - 1, -1):
#             current = array[i][start_col]
#             array[i][start_col] = prev
#             prev = current

#         start_col += 1

#     return array
