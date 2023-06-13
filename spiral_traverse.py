# O(n) time | O(n) space - where n is the total number of elements in the array
def spiralTraverse(array):
    # Write your code here.
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

    
def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
        # Handle the edge case when there's a single row
        # in the middle of the matrix. In this case, we don't
        # want to double-count the values in this row, which
        # we've already counted in the first for loop above
        if startRow == endRow:
            break
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        # Handle the edge case when there's a single column
        # in the middle of the matrix. In this case, we don't
        # want to double-count the values in this column, which
        # we've already counted in the second for loop above
        if startCol == endCol:
            break
        result.append(array[row][startCol])

    spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)


# Solution 2
# O(n) time | O(n) space - where n is the total number of elements in the array
# def spiralTraverse(array):
#     # Write your code here.
#     result = []
#     startRow, endRow = 0, len(array) - 1
#     startCol, endCol = 0, len(array[0]) - 1

#     while startRow <= endRow and startCol <= endCol:
#         for col in range(startCol, endCol + 1):
#             result.append(array[startRow][col])

#         for row in range(startRow + 1, endRow + 1):
#             result.append(array[row][endCol])

#         for col in reversed(range(startCol, endCol)):
#             # Handle the edge case when there's a single row
#             # in the middle of the matrix. In this case, we don't
#             # want to double-count the values in this row, which
#             # we've already counted in the first for loop above
#             if startRow == endRow:
#                 break
#             result.append(array[endRow][col])

#         for row in reversed(range(startRow + 1, endRow)):
#             # Handle the edge case when there's a single column
#             # in the middle of the matrix. In this case, we don't
#             # want to double-count the values in this column, which
#             # we've already counted in the second for loop above
#             if startCol == endCol:
#                 break
#             result.append(array[row][startCol])

#         startRow += 1
#         endRow -= 1
#         startCol += 1
#         endCol -= 1

#     return result



# def spiralTraverse(array):
#     # Write your code here.
#     k, l, m, n = 0, 0, len(array), len(array[0])
#     result = []

#     while k < m and l < n:
#         for i in range(l, n):
#             result.append(array[k][i])
#         k += 1

#         for i in range(k, m):
#             result.append(array[i][n-1])
#         n -= 1

#         if k < m:
#             for i in range(n-1, l-1, -1):
#                 result.append(array[m-1][i])
#             m -= 1

#         if l < n:
#             for i in range(m-1, k-1, -1):
#                 result.append(array[i][l])
#             l += 1
#     return result