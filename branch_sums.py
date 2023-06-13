# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def branchSums(root):
    # Write your code here.
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, currentSum, sums):
    if node is None:
        return

    newCurrentSum = currentSum + node.value
    if node.left is None and node.right is None:
        sums.append(newCurrentSum)
        return

    calculateBranchSums(node.left, newCurrentSum, sums)
    calculateBranchSums(node.right, newCurrentSum, sums)