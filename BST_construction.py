# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        # Write your code here.
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def remove(self, value, parentNode=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right
                        currentNode.left = currentNode.right.left
                    else:
                        # This is a single-nodetre; do nothing.
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

# Solution 2
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Average: O(log(n)) time | O(log(n)) space
#     # Worst: O(n) time | O(n) space
#     def insert(self, value):
#         # Write your code here.
#         # Do not edit the return statement of this method.
#         if value < self.value:
#             if self.left is None:
#                 self.left = BST(value)
#             else:
#                 self.left.insert(value)
#         else:
#             if self.right is None:
#                 self.right = BST(value)
#             else:
#                 self.right.insert(value)
#         return self

#     # Average: O(log(n)) time | O(log(n)) space
#     # Worst: O(n) time | O(n) space
#     def contains(self, value):
#         # Write your code here.
#         if value < self.value:
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.contains(value)
#         elif value > self.value:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.contains(value)
#         else:
#             return True

#     # Average: O(log(n)) time | O(log(n)) space
#     # Worst: O(n) time | O(n) space
#     def remove(self, value, parent=None):
#         # Write your code here.
#         # Do not edit the return statement of this method.
#         if value < self.value:
#             if self.left is not None:
#                 self.left.remove(value, self)
#         elif value > self.value:
#             if self.right is not None:
#                 self.right.remove(value, self)
#         else:
#             if self.left is not None and self.right is not None:
#                 self.value = self.right.getMinValue()
#                 self.right.remove(self.value, self)
#             elif parent is None:
#                 if self.left is not None:
#                     self.value = self.left.value
#                     self.right = self.left.right
#                     self.left = self.left.left
#                 elif self.right is not None:
#                     self.value = self.right.value
#                     self.right = self.right.right
#                     self.left = self.right.left
#                 else:
#                     # This is a single-nodetre; do nothing.
#                     pass
#             elif parent.left == self:
#                 parent.left = self.left if self.left is not None else self.right
#             elif parent.right == self:
#                 parent.right = self.left if self.left is not None else self.right
#         return self

#     def getMinValue(self):
#         if self.left is None:
#             return self.value
#         else:
#             return self.left.getMinValue()
