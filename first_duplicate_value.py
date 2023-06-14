# O(n) time | O(1) space - where n is the length of the input array
def firstDuplicateValue(array):
    # Write your code here.
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1



# Solution 2
# O(n) time | O(n) space - where n is the length of the input array
# def firstDuplicateValue(array):
#     # Write your code here.
#     seen = set()
#     for value in array:
#         if value in seen:
#             return value
#         seen.add(value)
#     return -1



# Solution 3
# O(n^2) time | O(1) space - where n is the length of the input array
# def firstDuplicateValue(array):
#     # Write your code here.
#     minimumSecondIndex = len(array)
#     for i in range(len(array)):
#         value = array[i]
#         for j in range(i + 1, len(array)):
#             valueToCompare = array[j]
#             if value == valueToCompare:
#                 minimumSecondIndex = min(minimumSecondIndex, j)

#     if minimumSecondIndex == len(array):
#         return -1

#     return array[minimumSecondIndex]
