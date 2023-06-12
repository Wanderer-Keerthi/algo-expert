# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(d) time | O(1) space - where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    searchOne = nodeOne
    searchTwo = nodeThree

    while True:
        foundThreeFromOne = searchOne is nodeThree
        foundOneFromThree = searchTwo is nodeOne
        foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        finishedSearching = searchOne is None and searchTwo is None
        if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishedSearching:
            break

        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right

        if searchTwo is not None:
            searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

    foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
    foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
    if not foundNodeTwo or foundNodeFromOther:
        return False
            
    return searchForTarget(nodeTwo, nodeThree if searchOne is nodeTwo else nodeOne)

def searchForTarget(node, target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target


# Solution 2
# This is an input class. Do not edit.
# class BST:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # O(h) time | O(1) space - where h is the height of the tree
# def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
#     # Write your code here.
#     if isDescendant(nodeTwo, nodeOne):
#         return isDescendant(nodeThree, nodeTwo)

#     if isDescendant(nodeTwo, nodeThree):
#         return isDescendant(nodeOne, nodeTwo)
    
#     return False

# # Whether the `target is a descendant of the `node`.
# def isDescendant(node, target):
#     while node is not None and node is not target:
#         node = node.left if target.value < node.value else node.right
        
#     return node is target


# Solution 3
# This is an input class. Do not edit.
# class BST:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # O(h) time | O(h) space - where h is the height of the tree
# def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
#     # Write your code here.
#     if isDescendant(nodeTwo, nodeOne):
#         return isDescendant(nodeThree, nodeTwo)

#     if isDescendant(nodeTwo, nodeThree):
#         return isDescendant(nodeOne, nodeTwo)
    
#     return False

# # Whether the `target is a descendant of the `node`.
# def isDescendant(node, target):
#     if node is None:
#         return False

#     if node is target:
#         return True

#     return isDescendant(node.left, target) if target.value < node.value else isDescendant(node.right, target)
