# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def middleNode(linkedList):
    # Write your code here.
    slowNode = linkedList
    fastNode = linkedList
    while fastNode and fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode



# Solution 2
# This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # O(n) time | O(1) space - where n is the number of nodes in the Linked List
# def middleNode(linkedList):
#     # Write your code here.
#     count = 0
#     currentNode = linkedList
#     while currentNode is not None:
#         count += 1
#         currentNode = currentNode.next

#     middleNode = linkedList
#     for _ in range(count // 2):
#         middleNode = middleNode.next
#     return middleNode
