# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
def largestBstSize(tree):
    # Write your code here.
    return getTreeInfo(tree).runningLargestBstSize


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(
            True,
            float("-inf"),
            float("inf"),
            0,
            0,
        )

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    treeSize = 1 + leftTreeInfo.treeSize + rightTreeInfo.treeSize

    satisfiesBstProp = tree.value > leftTreeInfo.maxValue and tree.value <= rightTreeInfo.minValue
    isBst = satisfiesBstProp and leftTreeInfo.isBst and rightTreeInfo.isBst

    maxValue = max(tree.value, max(leftTreeInfo.maxValue, rightTreeInfo.maxValue))
    minValue = min(tree.value, min(leftTreeInfo.minValue, rightTreeInfo.minValue))

    runningLargestBstSize = 0
    if isBst:
        runningLargestBstSize = treeSize
    else:
        runningLargestBstSize = max(leftTreeInfo.runningLargestBstSize, rightTreeInfo.runningLargestBstSize)

    return TreeInfo(
        isBst,
        maxValue,
        minValue,
        runningLargestBstSize,
        treeSize,
    )


class TreeInfo:
    def __init__(self, isBst, maxValue, minValue, runningLargestBstSize, treeSize):
        self.isBst = isBst
        self.maxValue = maxValue
        self.minValue = minValue
        self.runningLargestBstSize = runningLargestBstSize
        self.treeSize = treeSize


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# The solution to this question is straightforward from a conceptual point of view but tricky in its implementation.

# The overarching idea behind the solution is to traverse through the input binary tree once, to check at every node if the subtree rooted at that node is a BST, and to keep track of the largest found BST.

# Traversing through the tree is trivial. As for checking if a subtree is a BST, we need to specifically check that four conditions are met:

# 1) The left subtree of the current node is itself a BST.
# 2) The right subtree of the current node is itself a BST.
# 3) The current node's value is strictly greater than the max value in its left subtree.
# 4) The current node's value is lesser than or equal to the min value in its right subtree.
# This means that, as we traverse the tree, we need each node to return information to its parent node. Specifically, we need each node to provide whether its subtree is a BST, what its subtree's min and max values are, and of course, its subtree's size as well as the size of the largest BST found in its subtree.

# Note that the size of each subtree isn't necessarily needed, since we have the running largest BST size at every node, but it arguably makes the code a little easier to read.

#  Complexity Analysis

# This question is solved in linear time, since we traverse through each node only once and perform only constant-time operations at each node, and with a space complexity of O(h), where h is the height of the tree, which comes from the recursive aspect of the solution.

#  Closing Thoughts

# This is a classic BST question that assesses your ability to traverse trees, all the while passing information up from children nodes to their parent nodes.



# def findSize(tree):
#     if tree is None:
#         return 0

#     return findSize(tree.left) + 1 + findSize(tree.right)


# def isBST(node, min_value, max_value):
#     if node is None:
#         return True

#     if node.value < min_value or node.value >= max_value:
#         return False

#     return isBST(node.left, min_value, node.value) and isBST(node.right, node.value, max_value)


# def largestBstSize(tree):
#     # Write your code here.
#     if isBST(tree, float('-inf'), float('inf')):
#         return findSize(tree)

#     return max(largestBstSize(tree.left), largestBstSize(tree.right))

# # This is an input class. Do not edit.
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
