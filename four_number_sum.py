# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^2) space
def fourNumberSum(array, targetSum):
    # Write your code here.
    allPairSum = {}
    result = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSum:
                for pair in allPairSum[difference]:
                    result.append(pair + [array[i], array[j]])
        
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSum:
                allPairSum[currentSum] = [[array[i], array[k]]]
            else:
                allPairSum[currentSum].append([array[i], array[k]])

    return result
