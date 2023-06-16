# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space - where n is the length of the
# first Linked List, and m is the length of the second Linked List
def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo
    
    while currentNodeOne is not currentNodeTwo:
        if not currentNodeOne:
            currentNodeOne = linkedListTwo
        else:
            currentNodeOne = currentNodeOne.next

        if not currentNodeTwo:
            currentNodeTwo = linkedListOne
        else:
            currentNodeTwo = currentNodeTwo.next
        
    return currentNodeOne



# This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # O(n + m) time | O(1) space - where n is the length of the
# # first Linked List, and m is the length of the second Linked List
# def mergingLinkedLists(linkedListOne, linkedListTwo):
#     # Write your code here.
#     currentNodeOne = linkedListOne
#     countOne = 0
#     while currentNodeOne is not None:
#         countOne += 1
#         currentNodeOne = currentNodeOne.next

#     currentNodeTwo = linkedListTwo
#     countTwo = 0
#     while currentNodeTwo is not None:
#         countTwo += 1
#         currentNodeTwo = currentNodeTwo.next

#     difference = abs(countTwo - countOne)
#     biggerCurrentNode = linkedListOne if countOne > countTwo else linkedListTwo
#     smallerCurrentNode = linkedListTwo if countOne >  countTwo else linkedListOne
    
#     for _ in range(difference):
#         biggerCurrentNode = biggerCurrentNode.next

#     while biggerCurrentNode is not smallerCurrentNode:
#         biggerCurrentNode = biggerCurrentNode.next
#         smallerCurrentNode = smallerCurrentNode.next
        
#     return biggerCurrentNode



# Solution 3
# This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # O(n + m) time | O(n) space - where n is the length of the
# # first Linked List, and m is the length of the second Linked List
# def mergingLinkedLists(linkedListOne, linkedListTwo):
#     # Write your code here.
#     listOneNodes = set()
#     currentNodeOne = linkedListOne
#     while currentNodeOne is not None:
#         listOneNodes.add(currentNodeOne)
#         currentNodeOne = currentNodeOne.next

#     currentNodeTwo = linkedListTwo
#     while currentNodeTwo is not None:
#         if currentNodeTwo in listOneNodes:
#             return currentNodeTwo
#         currentNodeTwo = currentNodeTwo.next

#     return None
