# O(nlog(m)) time | O(1) space - where n is the number
# of build runs and m is the length of the longest build run
def buildFailures(buildRuns):
    # Write your code here.
    longestLength = 1
    currentLongestLength = 1
    previousGreenPercentage = calculatedGreenPercentage(buildRuns[0])

    for i in range(1, len(buildRuns)):
        currentGreenPercentage = calculatedGreenPercentage(buildRuns[i])
        if currentGreenPercentage < previousGreenPercentage:
            currentLongestLength += 1
            longestLength = max(longestLength, currentLongestLength)
        else:
            currentLongestLength = 1
        previousGreenPercentage = currentGreenPercentage

    return longestLength if longestLength > 1 else -1


def calculatedGreenPercentage(buildRun):
    firstFalseIdx = binarySearchForFirstFalse(buildRun)
    return firstFalseIdx / len(buildRun)


# Iterative Binary Search.
def binarySearchForFirstFalse(array):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx <= rightIdx:
        middleIdx = (leftIdx + rightIdx) // 2
        isFalse = not array[middleIdx]
        if isFalse:
            isFirstFalse = middleIdx == 0 or array[middleIdx - 1]
            if isFirstFalse:
                return middleIdx
            else:
                rightIdx = middleIdx - 1
        else:
            leftIdx = middleIdx + 1

    return -1




# O(nlog(m)) time | O(n + log(m)) space - where n is the number
# of build runs and m is the length of the longest build run
# def buildFailures(buildRuns):
#     # Write your code here.
#     greenPercentages = list(map(calculatedGreenPercentage, buildRuns))
#     return getLongestDecreasingSubarrayLength(greenPercentages)


# def calculatedGreenPercentage(buildRun):
#     firstFalseIdx = binarySearchForFirstFalse(buildRun, 0, len(buildRun) - 1)
#     return firstFalseIdx / len(buildRun)

# # Recursive Binary Search.
# def binarySearchForFirstFalse(array, leftIdx, rightIdx):
#     if leftIdx > rightIdx:
#         return -1

#     middleIdx = (leftIdx + rightIdx) // 2
#     isFalse = not array[middleIdx]
#     if isFalse:
#         isFirstFalse = middleIdx == 0 or array[middleIdx - 1]
#         if isFirstFalse:
#             return middleIdx
#         else:
#             return binarySearchForFirstFalse(array, leftIdx, middleIdx - 1)
#     else:
#         return binarySearchForFirstFalse(array, middleIdx + 1, rightIdx)


# def getLongestDecreasingSubarrayLength(array):
#     longestLength = 1
#     currentLongestLength = 1

#     for i in range(1, len(array)):
#         if array[i] < array[i - 1]:
#             currentLongestLength += 1
#             longestLength = max(longestLength, currentLongestLength)
#         else:
#             currentLongestLength = 1

#     return longestLength if longestLength > 1 else -1




# The first difficulty that this question introduces is the amount of information that it gives you. In order to grasp what this question is asking, you have to parse a lot of information.

# In a real interview, it would be important to ask clarifying questions in order to make sure that you correctly understand what the problem is asking.

# In this case, the problem gives us a list of build runs--lists of booleans specifically structured as [true, true, ..., true, false, false, ..., false]--and it wants us to return the length of the longest stretch of build runs in which the numbers of trues, proportionally speaking, are strictly decreasing.

# At face value, it seems like the hard part of this problem is going to be finding this longest stretch.

# After all, we can trivially compute the green percentages by finding the index of the first false in each build run and dividing it by the length of the respective build run.

# To find the first falses, we can simply iterate through each build run.

# ...Except, this is actually where we can optimize the solution to this problem. Instead of iterating through each build run, which would be a linear-time operation for each build run, we can cleverly use binary search to find the first falses and to improve this operation to log(n) time.

# As far as finding the longest stretch of strictly decreasing green percentages, this is actually a fairly straightforward algorithm to implement; the code should speak for itself.

#  Complexity Analysis

# We'll have to perform binary search, which is an O(log(m)) operation, where m is the length of the longest build run, n times--once on each build run. So the time complexity of our algorithm is going to be O(nlog(m)).

# We can perform the algorithm with constant space by not actually storing every green percentage, but instead only storing the last two green percentages as we iterate through the build runs and find the longest streak.

# Implementing our binary search iteratively will ensure that we don't use up auxiliary space because of recursion.

#  Closing Thoughts

# As mentioned above, this question is difficult in large part because of the amount of information that you have to parse in order to get started.

# It's also difficult because it camouflages the step of finding the first false in each build run, which is the meatiest step of the solution--the step where we use binary search. It's very easy to think that the main focus of our algorithm will be on finding the longest streak and to therefore gloss over the optimization with binary search.


