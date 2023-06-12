# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue


# O(h + k) time | O(h) space - where h is the height of the tree and k is the input parameter  
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
    if node is None or treeInfo.numberOfNodesVisited >= k:
        return

    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)



# Solution 2
# This is an input class. Do not edit.
# class BST:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# # O(n) time | O(n) space - where n is the number of nodes in the tree
# def findKthLargestValueInBst(tree, k):
#     # Write your code here.
#     sortedNodeValues = []
#     inOrderTraverse(tree, sortedNodeValues)
#     return sortedNodeValues[len(sortedNodeValues) - k]


# def inOrderTraverse(node, sortedNodeValues):
#     if node is None:
#         return

#     inOrderTraverse(node.left, sortedNodeValues)
#     sortedNodeValues.append(node.value)
#     inOrderTraverse(node.right, sortedNodeValues)
