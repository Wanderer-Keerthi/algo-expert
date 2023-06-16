# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def zipLinkedList(linkedList):
    # Write your code here.
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList

    firstHalfHead = linkedList
    secondHalfHead = splitLinkedList(linkedList)

    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)

    return interweaveLinkedList(firstHalfHead, reversedSecondHalfHead)


def splitLinkedList(linkedList):
    slowIterator = linkedList
    fastIterator = linkedList
    while fastIterator is not None and fastIterator.next is not None:
        slowIterator = slowIterator.next
        fastIterator = fastIterator.next.next

    secondHalfHead = slowIterator.next
    slowIterator.next = None
    return secondHalfHead


def interweaveLinkedList(linkedList1, linkedList2):
    linkedList1Iterator = linkedList1
    linkedList2Iterator = linkedList2
    while linkedList1Iterator is not None and linkedList2Iterator is not None:
        linkedList1IteratorNext = linkedList1Iterator.next
        linkedList2IteratorNext = linkedList2Iterator.next

        linkedList1Iterator.next = linkedList2Iterator
        linkedList2Iterator.next = linkedList1IteratorNext

        linkedList1Iterator = linkedList1IteratorNext
        linkedList2Iterator = linkedList2IteratorNext

    return linkedList1


def reverseLinkedList(linkedList):
    previousNode, currentNode = None, linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
