# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | 0(1) space - where n is thenumberof nodes in the Linked List
def invertedBisection(head):
    # Write your code here.
    length = getLinkedListLength(head)
    if length <= 3:
        return head
    
    firstHalfTail = getMiddleNode(head, length)
    middleNode = None
    secondHalfHead = None
    if length % 2 == 0:
        secondHalfHead = firstHalfTail.next
    else:
        middleNode = firstHalfTail.next
        secondHalfHead = firstHalfTail.next.next
    
    firstHalfTail.next = None
    reverseLinkedList(head)
    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)

    if middleNode is None:
        head.next = reversedSecondHalfHead
    else:
        head.next = middleNode
        middleNode.next = reversedSecondHalfHead
        
    return firstHalfTail


def getLinkedListLength(head):
    length = 0
    currentNode = head
    while currentNode is not None:
        currentNode = currentNode.next
        length += 1
    return length


def getMiddleNode(head, length):
    halfLength = length // 2
    currentPosition = 1
    currentNode = head
    while currentPosition != halfLength:
        currentNode = currentNode.next
        currentPosition += 1
    return currentNode


def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode



# The solution to this question can be divided into four parts:

# 1) Counting the number of nodes in the linked list.
# 2) Splitting the linked list into two equal halves.
# 3) Reversing the two halves of the linked list.
# 4) Reattaching the two reversed halves.
#  1) Counting the nodes

# This step is done trivially by simply iterating through the linked list and incrementing a counter at every node.

#  2) Splitting the linked list

# For this step, we first iterate through the linked list up to its halfway point, basing ourselves off of its previously calculated length.

# At this point, we have to handle the trickiness that comes with an odd-length linked list. An odd-length linked list will have a middle node that should remain unmoved in the final linked list. To handle this, we keep a reference to the middle node if the linked list is of odd length before splitting the list in half.

# The split is done by simply overwriting the first half's tail's next pointer.

# In this process, we'll naturally keep references to the first half's tail and to the second half's head.

#  3) Reversing the two halves

# This step is very straightforward, but you'll need to know how to reverse a linked list; see the Reverse Linked List question on AlgoExpert if you need a refresher.

# We simply write a helper function to reverse a linked list, and we call it on the two halves. We'll need to store a reference to the head of the reversed second half for the final step.

#  4) Reattaching the two halves

# Keeping in mind the trickiness of the middle node, we handle this step slightly differently depending on whether the linked list is of odd length.

# If it is of odd length, then the tail of the reversed first half--which is the head of the original linked list--should point to the stored middle node, and the middle node should in turn point to the head of the reversed second half.

# If it isn't of odd length, then the tail of the reversed first half should directly point to the head of the reversed second half.

#  Complexity Analysis

# This question is self-evidently solved in linear time and with constant space.

#  Closing Thoughts

# As with most Linked List problems, this question's difficulty lies in handling edge cases, overwriting pointers appropriately, and keeping references to certain nodes.

# Oh, and reversing linked lists of course!