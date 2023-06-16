# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def nodeSwap(head):
    # Write your code here.
    tempNode = LinkedList(0)
    tempNode.next = head

    prevNode = tempNode
    while prevNode.next is not None and prevNode.next.next is not None:
        firstNode = prevNode.next
        secondNode = prevNode.next.next
        # prevNode -> firstNode -> secondNode -> x

        firstNode.next = secondNode.next
        secondNode.next = firstNode
        prevNode.next = secondNode
        # prevNode -> secondNode -> firstNode -> x

        prevNode = firstNode
        
    return tempNode.next



# Solution 2
# This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # O(n) time | O(n) space - where n is the number of nodes in the Linked List
# def nodeSwap(head):
#     # Write your code here.
#     if head is None or head.next is None:
#         return head

#     nextNode = head.next
#     head.next = nodeSwap(head.next.next)
#     nextNode.next = head
#     return nextNode
