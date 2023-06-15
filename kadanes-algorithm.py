# O(n) time | O(1) space - where n is the length of the input array
def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar



# Solution 2 
# def kadanesAlgorithm(array):
#     # Write your code here.
#     resultSum, intermediateSum = array[0], 0

#     for idx in range(len(array)):
#         intermediateSum += array[idx]

#         if array[idx] > intermediateSum:
#             intermediateSum = array[idx]
#         if intermediateSum > resultSum:
#             resultSum = intermediateSum

#     return resultSum