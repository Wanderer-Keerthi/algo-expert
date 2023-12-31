# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right -= 1
        elif currentSum  < targetSum:
            left += 1
    return []



# Solution 2
# O(n) time | O(n) space
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return [potentialMatch, num]
#         else:
#             nums[num] = True

#     return []


# Solution 3
# O(n^2) time | O(1) space
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]

#     return []
