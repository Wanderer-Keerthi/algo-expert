# O(n) time | O(n) space - where n is the length of the input array
def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares


# Solution 2
# O(nlogn) time | O(n) space - where n is the length of the input array
# def sortedSquaredArray(array):
#     # Write your code here.
#     sortedSquares = [0 for _ in array]

#     for idx in range(len(array)):
#         value = array[idx]
#         sortedSquares[idx] = value * value

#     sortedSquares.sort()
#     return sortedSquares


# Solution 3
# def sortedSquaredArray(array):
#     # Write your code here.
#     result = []
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         minVal = array[left]
#         maxVal = array[right]
#         if abs(minVal) > abs(maxVal):
#             val = minVal
#             left += 1
#         else:
#             val = maxVal
#             right -= 1
#         result = [val * val] + result
#     return result