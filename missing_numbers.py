# O(n) time | O(1) space - where n is the length of the input array
def missingNumbers(nums):
    # Write your code here.
    solutionXOR = 0
    for i in range(0, len(nums) + 3):
        solutionXOR ^= i
        if i < len(nums):
            solutionXOR ^= nums[i]

    solution = [0, 0]
    setBit = solutionXOR & -solutionXOR
    for i in range(0, len(nums) + 3):
        if i & setBit == 0:
            solution[0] ^= i
        else:
            solution[1] ^= i
        
        if i < len(nums):
            if nums[i] & setBit == 0:
                solution[0] ^= nums[i]
            else:
                solution[1] ^= nums[i]
                
    return sorted(solution)



# Solution 2
# O(n) time | O(1) space - where n is the length of the input array
# def missingNumbers(nums):
#     # Write your code here.
#     total = sum(range(1, len(nums) + 3))
#     for num in nums:
#         total -= num

#     averageMissingValue = total // 2
#     foundFirstHalf = 0
#     foundSecondHalf = 0
#     for num in nums:
#         if num <= averageMissingValue:
#             foundFirstHalf += num
#         else:
#             foundSecondHalf += num

#     expectedFirstHalf = sum(range(1, averageMissingValue + 1))
#     expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))

#     return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]



# Solution 3
# O(n) time | O(n) space - where n is the length of the input array
# def missingNumbers(nums):
#     # Write your code here.
#     includedNums = set(nums)

#     solution = []
#     for num in range(1, len(nums) + 3):
#         if not num in includedNums:
#             solution.append(num)
            
#     return solution
