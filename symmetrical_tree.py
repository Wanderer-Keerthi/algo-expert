# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space - where n is the number of nodes in the tree
#  and h is the height of the tree.
def symmetricalTree(tree):
    # Write your code here.
    return treesAreMirrored(tree.left, tree.right)

def treesAreMirrored(left, right):
    if left is not None and right is not None and left.value == right.value:
        return treesAreMirrored(left.left, right.right) and treesAreMirrored(left.right, right.left)

    return left == right

# Solution 2
# This is an input class. Do not edit.
# class BinaryTree:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # O(n) time | O(h) space - where n is the number of nodes in the tree
# #  and h is the height of the tree.
# def symmetricalTree(tree):
#     # Write your code here.
#     stackLeft = [tree.left]
#     stackRight = [tree.right]

#     while len(stackLeft) > 0:
#         left = stackLeft.pop()
#         right = stackRight.pop()

#         if left is None and right is None:
#             continue

#         if left is None or right is None or left.value != right.value:
#             return False

#         stackLeft.append(left.left)
#         stackLeft.append(left.right)
#         stackRight.append(right.right)
#         stackRight.append(right.left)

#     return True

# Solution 3
# This is an input class. Do not edit.
# class BinaryTree:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# def symmetricalTree(tree):
#     # Write your code here.
#     def symmetricalTreeHelper(root_left, root_right):
#         if not root_left and not root_right:
#             return True
#         elif root_left and root_right and root_left.value == root_right.value:
#             return symmetricalTreeHelper(root_left.right, root_right.left) and symmetricalTreeHelper(root_left.left, root_right.right)
#         return False
    
#     return symmetricalTreeHelper(tree, tree)