# O(n * m) time | O(n * m) space - where n is th length of the
# first input array and m is the length of the second input array
def maxSubsequenceDotProduct(arrayOne, arrayTwo):
    # Write your code here.
    maxDotProducts = initializeDotProducts(arrayOne, arrayTwo)
    for i in range(1, len(arrayOne) + 1):
        for j in range(1, len(arrayTwo) + 1):
            currentProduct = arrayOne[i - 1] * arrayTwo[j - 1]
            maxDotProducts[i][j] = max(
                currentProduct,
                maxDotProducts[i - 1][j - 1] + currentProduct,
                maxDotProducts[i - 1][j - 1],
                maxDotProducts[i - 1][j],
                maxDotProducts[i][j - 1],
            )
    return maxDotProducts[len(arrayOne)][len(arrayTwo)]


def initializeDotProducts(arrayOne, arrayTwo):
    dotProducts = [[float("-inf") for j in range(len(arrayTwo) + 1)] for i in range(len(arrayOne) + 1)]
    return dotProducts



# This question is a classic dynamic programming question. If we try to solve it using a brute-force approach, we quickly realize that we'll be doing far too many operations, and even getting a brute-force approach to work is a brain twister.

# The most straightforward way to solve the question is to build up a table--a two-dimensional array--containing various max dot products.

# Specifically, the table's dimensions will be (n + 1) * (m + 1), where n and m are the respective lengths of the input arrays, and each value in the table at indices (i, j) will represent the max dot product that we can obtain if the arrays stopped at indices i - 1 and j - 1, respectively.

# The first row and column will represent the empty arrays.

# The values in the first row and in the first column will be set to negative infinity, since if one of the two arrays is empty, there is no obtainable dot product.

# Then, as we iterate through the table, row by row and column by column, we'll calculate the currentProduct of the i - 1th and j - 1th numbers and we'll populate each table cell by taking the max value of five options:

# 1) The currentProduct alone. If any previous max dot product brings this value down, then we want to isolate this value.
# 2) The max dot product of the two arrays without the i - 1th and j - 1th elements, plus the currentProduct. This is if we want to add the currentProduct to a previous max dot product.
# 3) The max dot product of the two arrays without the i - 1th and j - 1th elements alone. If the currentProduct brings our previous max product dot product down, we don't want to add it.
# 4) The max dot product of the two arrays without the j - 1th element. If the i - 1th element brings our previous max product dot product down, we don't want to add it.
# 5) The max dot product of the two arrays without the i - 1th element. If the j - 1th element brings our previous max product dot product down, we don't want to add it.
# The final table for the sample input of this question will look like:

#          5,  1, -1, -3, -2, -10
#      -,  -,  -,  -,  -,  -,
#   4, -, 20, 20, 20, 20, 20,  20
#   7, -, 35, 35, 35, 35, 35,  35
#   9, -, 45, 45, 45, 45, 45,  45 
#  -6, -, 45, 45, 51, 63, 63, 105
#   6, -, 45, 51, 51, 63, 63, 105
# We can clearly see that in the bottom right corner of the table, we have the max dot product of the entire two arrays.

#  Complexity Analysis

# As for with many dynamic programming questions, we can deduce the time and space complexities of this solution pretty easily since all that we're really doing is creating a two-dimensional array and traversing it, performing constant-time operations at every step.

# Since the table's dimensions are based off of the two input arrays, the time and space complexities of the solution are both going to be O(n * m), where n and m are the respective lengths of the arrays.

#  Closing Thoughts

# As mentioned above, this is a classic dynamic programming question that is best solved by writing out the table of the two arrays and trying to figure out what relations between cells make the most sense.



# def maxSubsequenceDotProduct(arrayOne, arrayTwo):
#     # Write your code here.
#     m = len(arrayOne)
#     n = len(arrayTwo)

#     # Initialize a dynamic programming table
#     dp = [[0] * (n + 1) for _ in range(m + 1)]

#     # Fill in the table using dynamic programming
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             # Calculate the dot product of the current elements
#             product = arrayOne[i - 1] * arrayTwo[j - 1]

#             # Choose whether to include the current elements or not
#             dp[i][j] = max(dp[i - 1][j - 1] + product, dp[i][j - 1], dp[i - 1][j])

#     # Return the maximum dot product
#     return dp[m][n]
            
