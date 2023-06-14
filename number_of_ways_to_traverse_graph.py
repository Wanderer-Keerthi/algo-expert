# O(n + m) time | O(1) space - where n
# is the width of the graph and m is the height
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    xDistanceToCorner = width - 1
    yDistanceToCorner = height - 1

    # The number of permutations of right and down movements
    # is the number of ways to reach the bottom right corner.
    numerator = factorial(xDistanceToCorner + yDistanceToCorner)
    denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)
    return numerator // denominator


def factorial(num):
    result = 1

    for n in range(2, num + 1):
        result *= n
        
    return result



# Solution 2
# O(n * m) time | O(n * m) space - where n
# is the width of the graph and m is the height
# def numberOfWaysToTraverseGraph(width, height):
#     # Write your code here.
#     numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

#     for widthIdx in range(1, width + 1):
#         for heightIdx in range(1, height + 1):
#             if widthIdx == 1 or heightIdx == 1:
#                 numberOfWays[heightIdx][widthIdx] = 1
#             else:
#                 waysLeft = numberOfWays[heightIdx][widthIdx - 1]
#                 waysUp = numberOfWays[heightIdx - 1][widthIdx]
#                 numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp
                
#     return numberOfWays[height][width]



# Solution 3
# O(2^(n + m)) time | O(n + m) space - where n
# is the width of the graph and m is the height
# def numberOfWaysToTraverseGraph(width, height):
#     # Write your code here.
#     if width == 1 or height == 1:
#         return 1
        
#     return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)
