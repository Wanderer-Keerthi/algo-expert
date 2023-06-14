# O(n^2) time | O(n) space - where n is the length of prices
def juiceBottling(prices):
    # Write your code here.
    numSizes = len(prices)
    maxProfit = [0] * numSizes
    dividingPoints = [0] * numSizes

    for size in range(numSizes):
        for dividingPoint in range(size + 1):
            possibleProfit = maxProfit[size - dividingPoint] + prices[dividingPoint]

            if possibleProfit > maxProfit[size]:
                maxProfit[size] = possibleProfit
                dividingPoints[size] = dividingPoint

    solution = []
    currentDividingPoint = numSizes - 1
    while currentDividingPoint > 0:
        solution.append(dividingPoints[currentDividingPoint])
        currentDividingPoint -= dividingPoints[currentDividingPoint]
        
    return solution



# Solution 2
# O(n^3) time | O(n^2) space - where n is the length of prices
# def juiceBottling(prices):
#     # Write your code here.
#     numSizes = len(prices)
#     maxProfit = [0] * numSizes
#     solutions = [[]] * numSizes

#     for size in range(numSizes):
#         for dividingPoint in range(size + 1):
#             possibleProfit = maxProfit[size - dividingPoint] + prices[dividingPoint]

#             if possibleProfit > maxProfit[size]:
#                 maxProfit[size] = possibleProfit
#                 solutions[size] = [dividingPoint] + solutions[size - dividingPoint]
                
#     return solutions[numSizes - 1]
