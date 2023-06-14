# O(n) time | O(n) space - where n is the length of the array
def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4:
        return 0

    maxOfA = [array[0]]
    maxOfAMinusB = [float("-inf")]
    maxOfAMinusBPlusC = [float("-inf")] * 2
    maxOfAMinusBPlusCMinusD = [float("-inf")] * 3

    for idx in range(1, len(array)):
        currentMax = max(maxOfA[idx - 1], array[idx])
        maxOfA.append(currentMax)

    for idx in range(1, len(array)):
        currentMax = max(maxOfAMinusB[idx - 1], maxOfA[idx - 1] - array[idx])
        maxOfAMinusB.append(currentMax)

    for idx in range(2, len(array)):
        currentMax = max(maxOfAMinusBPlusC[idx - 1], maxOfAMinusB[idx - 1] + array[idx])
        maxOfAMinusBPlusC.append(currentMax)

    for idx in range(3, len(array)):
        currentMax = max(maxOfAMinusBPlusCMinusD[idx - 1], maxOfAMinusBPlusC[idx - 1] - array[idx])
        maxOfAMinusBPlusCMinusD.append(currentMax)

    return maxOfAMinusBPlusCMinusD[len(maxOfAMinusBPlusCMinusD) - 1]


# Solution 2
# O(n^4) time | O(1) space - where n is the length of the array
# def maximizeExpression(array):
#     # Write your code here.
#     if len(array) < 4:
#         return 0 

#     maximumValueFound = float("-inf")

#     for a in range(len(array)):
#         aValue = array[a]
#         for b in range(a + 1, len(array)):
#             bValue = array[b]
#             for c in range(b + 1, len(array)):
#                 cValue = array[c]
#                 for d in range(c + 1, len(array)):
#                     dValue = array[d]
#                     expressionValue = evaluateExpression(aValue, bValue, cValue, dValue)
#                     maximumValueFound = max(expressionValue, maximumValueFound)
    
#     return maximumValueFound


# def evaluateExpression(a, b, c, d):
#     return a - b + c - d
