# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(d) space - where n is the number of nodes in the Binary Tree
# and d is the depth (height) of the Binary Tree
def flattenBinaryTree(root):
    # Write your code here.
    leftMost, _ = flattenTree(root)
    return leftMost


def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connectNodes(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRightMost

    return [leftMost, rightMost]


def connectNodes(left, right):
    left.right = right
    right.left = left


# Solution 2
# This is the class of the input root. Do not edit it.
# class BinaryTree:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
# def flattenBinaryTree(root):
#     # Write your code here.
#     inOrderNodes = getNodesInOrder(root, [])
#     for i in range(0, len(inOrderNodes) - 1):
#         leftNode = inOrderNodes[i]
#         rightNode = inOrderNodes[i + 1]
#         leftNode.right = rightNode
#         rightNode.left = leftNode
#     return inOrderNodes[0]


# def getNodesInOrder(tree, array):
#     if tree is not None:
#         getNodesInOrder(tree.left, array)
#         array.append(tree)
#         getNodesInOrder(tree.right, array)
#     return array

