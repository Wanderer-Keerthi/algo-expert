# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    current = tree
    while current:
        if abs(target - closest) > abs(target - current.value):
            closest = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            break

    return closest

    
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

# Solution 2
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, tree.value)

# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     else:
#         return closest

    
# # This is the class of the input tree. Do not edit.
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

