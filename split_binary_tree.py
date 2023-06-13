# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the tree
#  and h is the height of the tree.
def splitBinaryTree(tree):
    # Write your code here.
    desiredSubtreeSum = getTreeSum(tree) / 2
    canBeSplit = trySubTrees(tree, desiredSubtreeSum)[1]
    return desiredSubtreeSum if canBeSplit else 0


def trySubTrees(tree, desiredSubtreeSum):
    if tree is None:
        return (0, False)

    leftSum, leftCanBeSplit = trySubTrees(tree.left, desiredSubtreeSum)
    rightSum, rightCanBeSplit = trySubTrees(tree.right, desiredSubtreeSum)

    currentTreeSum = tree.value + leftSum + rightSum
    canBeSplit = leftCanBeSplit or rightCanBeSplit or currentTreeSum == desiredSubtreeSum
    return (currentTreeSum, canBeSplit)

def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)

