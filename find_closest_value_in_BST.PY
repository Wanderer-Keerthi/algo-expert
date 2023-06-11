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
