# O(n) time | O(1) space - where n is the length of the input array
def longestStreakOfAdjacentOnes(array):
    # Write your code here.
    longestStreakLength = 0
    longestStreakReplacedZeroIdx = -1
    
    currentStreakLength = 0
    replacedZeroIdx = -1
    
    for i in range(len(array)):
        if array[i] == 1:
            currentStreakLength += 1
        else:
            currentStreakLength = i - replacedZeroIdx
            replacedZeroIdx = i

        if currentStreakLength > longestStreakLength:
            longestStreakLength = currentStreakLength
            longestStreakReplacedZeroIdx = replacedZeroIdx

    return longestStreakReplacedZeroIdx



# We can solve this question in one pass through the array. To do so, we'll need to keep track of four variables:

# The length of the longest streak of 1s.
# The index of the replaced 0 that yields the longest streak of 1s.
# The length of the current streak of 1s.
# The index of the currently replaced 0.
# As we iterate through the array, we treat every 0 that we encounter as the current 0 to replace. This means that, whenever we encounter a 0, we set the length of the current streak to index - replacedZeroIdx (this is the stretch of 1s between the previous 0 and the current 0) before updating the index of the replaced 0 to the index that we're at.

# Whenever we encounter a 1, we increment the length of the current streak of 1s, and regardless of what value we encounter, we check if we have to update the two variables for the longest streak of 1s by comparing the length of the current streak to the length of the longest streak.

#  Complexity Analysis

# This question is self-evidently solved in linear time and with constant space.

#  Closing Thoughts

# The algorithm behind this problem's optimal solution is tricky; it's important to walk through to an example and to ask yourself what exact information you have whenever you encounter a 0. This leads you to the algorithm presented above.

# The sequencing of operations in the solution's for loop is also very important.