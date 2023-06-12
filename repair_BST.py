# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the
# tree and h is the height of the tree
def repairBst(tree):
    # Write your code here.
    nodeOne = nodeTwo = previousNode = None

    stack = []
    currentNode = tree
    while currentNode is not None or len(stack) > 0:
        while currentNode is not None:
            stack.append(currentNode)
            currentNode = currentNode.left
        currentNode = stack.pop()

        if previousNode is not None and previousNode.value > currentNode.value:
            if nodeOne is None:
                nodeOne = previousNode
            nodeTwo = currentNode

        previousNode = currentNode
        currentNode = currentNode.right

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree


# Solution 2
# This is an input class. Do not edit.
# class BST:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # O(n) time | O(h) space - where n is the number of nodes in the
# # tree and h is the height of the tree
# def repairBst(tree):
#     # Write your code here.
#     nodeOne = nodeTwo = previousNode = None

#     def inOrderTraversal(node):
#         nonlocal nodeOne, nodeTwo, previousNode
#         if node is None:
#             return

#         inOrderTraversal(node.left)

#         if previousNode is not None and previousNode.value > node.value:
#             if nodeOne is None:
#                 nodeOne = previousNode
#             nodeTwo = node

#         previousNode = node
#         inOrderTraversal(node.right)

#     inOrderTraversal(tree)

#     nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
#     return tree
