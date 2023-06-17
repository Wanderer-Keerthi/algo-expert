# O(log(n)) time | O(1) space - where n is the length of the input array
def indexEqualsValue(array):
    # Write your code here.
    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        middleValue = array[middleIndex]
    
        if middleValue < middleIndex:
            leftIndex = middleIndex + 1
        elif middleValue == middleIndex and middleIndex == 0:
            return middleIndex
        elif middleValue == middleIndex and array[middleIndex - 1] < middleIndex - 1:
            return middleIndex
        else:
            rightIndex = middleIndex - 1

    return -1



# Solution 2
# O(log(n)) time | O(log(n)) space - where n is the length of the input array
# def indexEqualsValue(array):
#     # Write your code here.
#     return indexEqualsValueHelper(array, 0, len(array) - 1)


# def indexEqualsValueHelper(array, leftIndex, rightIndex):
#     if leftIndex > rightIndex:
#         return -1

#     middleIndex = leftIndex + (rightIndex - leftIndex) // 2
#     middleValue = array[middleIndex]

#     if middleValue < middleIndex:
#         return indexEqualsValueHelper(array, middleIndex + 1, rightIndex)
#     elif middleValue == middleIndex and middleIndex == 0:
#         return middleIndex
#     elif middleValue == middleIndex and array[middleIndex - 1] < middleIndex - 1:
#         return middleIndex
#     else:
#         return indexEqualsValueHelper(array, leftIndex, middleIndex - 1)



# Solution 3
# O(n) time | O(1) space - where n is the length of the input array
# def indexEqualsValue(array):
#     # Write your code here.
#     for index in range(len(array)):
#         value = array[index]
#         if index == value:
#             return index

#     return -1
