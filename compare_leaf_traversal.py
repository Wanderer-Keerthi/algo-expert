class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n + m) time | O(max(h1, h2)) space - where n is the number of nodes in the first
# Binary Tree, m is the number in the second, h1 is the height of the first Binary
# Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    # Write your code here.
    tree1LeafNodesLinkedList, _ = connectLeafNodes(tree1)
    tree2LeafNodesLinkedList, _ = connectLeafNodes(tree2)
    
    list1CurrentNode = tree1LeafNodesLinkedList
    list2CurrentNode = tree2LeafNodesLinkedList
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value:
            return False

        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right

    return list1CurrentNode is None and list2CurrentNode is None


def connectLeafNodes(currentNode, head=None, previousNode=None):
    if currentNode is None:
        return head, previousNode

    if isLeafNode(currentNode):
        if previousNode is None:
            head = currentNode
        else:
            previousNode.right = currentNode

        previousNode = currentNode

    leftHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)
    return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)


def isLeafNode(node):
    return node.left is None and node.right is None


# Solution 2
# This is an input class. Do not edit.
# class BinaryTree:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # O(n + m) time | O(h1 + h2) space - where n is the number of nodes in the first
# # Binary Tree, m is the number in the second, h1 is the height of the first Binary
# # Tree, and h2 is the height of the second
# def compareLeafTraversal(tree1, tree2):
#     # Write your code here.
#     tree1TraversalStack = [tree1]
#     tree2TraversalStack = [tree2]

#     while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0:
#         tree1Leaf = getNextLeafNode(tree1TraversalStack)
#         tree2Leaf = getNextLeafNode(tree2TraversalStack)

#         if tree1Leaf.value != tree2Leaf.value:
#             return False
        
#     return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0
    

# def getNextLeafNode(traversalStack):
#     currentNode = traversalStack.pop()

#     while not isLeafNode(currentNode):
#         if currentNode.right is not None:
#             traversalStack.append(currentNode.right)

#         # We purposely add the left node o the stack after thr
#         # right node so that it gets popped off the stack first.
#         if currentNode.left is not None:
#             traversalStack.append(currentNode.left)

#         currentNode = traversalStack.pop()

#     return currentNode


# def isLeafNode(node):
#     return node.left is None and node.right is None
    