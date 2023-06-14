# O(n) time | O(n) space - where n is the length of nums
def zeroSumSubarray(nums):
    # Write your code here.
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)

    return False



# Solution 2
# def zeroSumSubarray(nums):
#     # Write your code here.
#     hashMap = {}
#     sum = 0
#     for i in range(len(nums)):
#         sum += nums[i]

#         if sum == 0:
#             return True

#         if sum in hashMap:
#             return True
            
#         hashMap[sum] = i
#     return False
