# O(n) time | O(1) space - where n is the length of the input array
def longestSubarrayWithSum(array, targetSum):
    # Write your code here.
    indices = []

    currentSubarraySum = 0
    startingIndex = 0
    endingIndex = 0

    while endingIndex < len(array):
        currentSubarraySum += array[endingIndex]
        while startingIndex < endingIndex and currentSubarraySum > targetSum:
            currentSubarraySum -= array[startingIndex]
            startingIndex += 1

        if currentSubarraySum == targetSum:
            if len(indices) == 0 or indices[1] - indices[0] < endingIndex - startingIndex:
                indices = [startingIndex, endingIndex]

        endingIndex += 1

    return indices



# Solution 2
# O(n^2) time | O(1) space - where n is the length of the input array
# def longestSubarrayWithSum(array, targetSum):
#     # Write your code here.
#     indices = []

#     for startingIndex in range(len(array)):
#         currentSubarraySum = 0

#         for endingIndex in range(startingIndex, len(array)):
#             currentSubarraySum += array[endingIndex]

#             if currentSubarraySum == targetSum:
#                 if len(indices) == 0 or indices[1] - indices[0] < endingIndex - startingIndex:
#                     indices = [startingIndex, endingIndex]

#     return indices
