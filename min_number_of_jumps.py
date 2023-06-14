# O(n) time | O(1) space
def minNumberOfJumps(array):
    # Write your code here.
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1



# Solution 2
# O(n^2) time | O(n) space
# def minNumberOfJumps(array):
#     # Write your code here.
#     jumps = [float("inf") for x in array]
#     jumps[0] = 0
#     for i in range(1, len(array)):
#         for j in range(0, i):
#             if array[j] >= i - j:
#                 jumps[i] = min(jumps[j] + 1, jumps[i])
#     return jumps[-1]



# Solution 3
# def minNumberOfJumps(array):
#     # Write your code here.
#     jump = 1
#     a, b = array[0], array[0]
#     if len(array) == 0 or len(array) == 1:
#         return 0

#     for i in range(1, len(array)):
#         if i == len(array) - 1:
#             return jump

#         a -= 1
#         b -= 1
#         if array[i] > b:
#             b = array[i]

#         if a == 0:
#             a = b
#             jump += 1
#     return jump
