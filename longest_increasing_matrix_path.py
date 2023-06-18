# O(n) time | O(n) space - where n is the total number of elements in the matrix
def longestIncreasingMatrixPath(matrix):
    # Write your code here.
    longestPathLengths = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(None)
        longestPathLengths.append(row)
    
    longestPathLength = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            longestPathLength = max(
                getLongestPathLengthAt(matrix, row, col, float("-inf"), longestPathLengths),
                longestPathLength,
            )
    
    return longestPathLength


def getLongestPathLengthAt(matrix, row, col, lastPathValue, longestPathLengths):
    isOutOfBounds = row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])
    if isOutOfBounds:
        return 0
    
    currentValue = matrix[row][col]
    if currentValue <= lastPathValue:
        return 0
    
    if longestPathLengths [row][col] is None:
        longestPathLengths [row][col] = 1 + max(
            getLongestPathLengthAt(matrix, row- 1, col, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row + 1, col, currentValue, longestPathLengths), 
            getLongestPathLengthAt(matrix, row, col - 1, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row, col + 1, currentValue, longestPathLengths),
        )
    
    return longestPathLengths[row][col]




# There are two ways of solving this question, both involving a single traversal of the input BST. While both are viable solutions with the same complexity ramifications, the second solution is a little simpler to code out and arguably cleaner.

#  Solution 1

# For the first solution, we'll recursively traverse through the tree and have every node return three values to its parent node:

# 1) The min value in the subtree rooted at the node.
# 2) The max value in the subtree rooted at the node.
# 3) The number of subtrees in the subtree rooted at the node that are within the target range.
# With these values from its children nodes, each node will be able to tell if the subtree rooted at itself is within the target range, since it'll have the left subtree's min value and the right subtree's max value (recall the BST property and what it tells us), and since each node will have the numbers of subtrees within the target range in its left and right subtrees.

# The root of the BST will therefore be given the total number of subtrees within the target range once the tree traversal is done.

#  Solution 2

# For the second solution, our recursive function will simply return whether or not the subtree rooted at the current node is within the target range.

# To do this, our function will recurively call itself on each current node's left and right children nodes, checking if the subtrees rooted at them are both within the target range, and it will check that each current node's value is within the target range.

# If these three conditions are met and the current subtree is therefore within the target range, the recursive function will increment some final counter.

# Note that this solution doesn't need to use anything about the BST property.

#  Complexity Analysis

# This question is solved in linear time, since we traverse through each node only once and perform only constant-time operations at each node, and with a space complexity of O(h), where h is the height of the tree, which comes from the recursive aspect of the solutions.

#  Closing Thoughts

# This is a classic BST question that assesses your ability to traverse trees, all the while passing information up from children nodes to their parent nodes in the case of the first solution.