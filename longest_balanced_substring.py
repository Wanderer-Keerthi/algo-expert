# O(n) time | O(1) space - where n is the length of the input string
def longestBalancedSubstring(string):
    # Write your code here.
    return max(
        getLongestBalancedInDirection(string, True),
        getLongestBalancedInDirection(string, False),
    )


def getLongestBalancedInDirection(string, leftToRight):
    openingParens = "(" if leftToRight else ")"
    startIdx = 0 if leftToRight else len(string) - 1
    step = 1 if leftToRight else -1

    maxLength = 0

    openingCount = 0
    closingCount = 0

    idx = startIdx
    while idx >= 0 and idx < len(string):
        char = string[idx]
        
        if char == openingParens:
            openingCount += 1
        else:
            closingCount += 1

        if openingCount == closingCount:
            maxLength = max(maxLength, closingCount * 2)
        elif closingCount > openingCount:
            openingCount = 0
            closingCount = 0

        idx += step

    return maxLength



# Solution 2
# O(n) time | O(1) space - where n is the length of the input string
# def longestBalancedSubstring(string):
#     # Write your code here.
#     maxLength = 0

#     openingCount = 0
#     closingCount = 0

#     for char in string:
#         if char == "(":
#             openingCount += 1
#         else:
#             closingCount += 1

#         if openingCount == closingCount:
#             maxLength = max(maxLength, closingCount * 2)
#         elif closingCount > openingCount:
#             openingCount = 0
#             closingCount = 0

#     openingCount = 0
#     closingCount = 0

#     for i in reversed(range(len(string))):
#         char = string[i]
         
#         if char == "(":
#             openingCount += 1
#         else:
#             closingCount += 1

#         if openingCount == closingCount:
#             maxLength = max(maxLength, openingCount * 2)
#         elif openingCount > closingCount:
#             openingCount = 0
#             closingCount = 0

#     return maxLength



# Solution 3
# O(n) time | O(n) space - where n is the length of the input string
# def longestBalancedSubstring(string):
#     # Write your code here.
#     maxLength = 0
#     idxStack = []
#     idxStack.append(-1)

#     for i in range(len(string)):
#         if string[i] == "(":
#             idxStack.append(i)
#         else:
#             idxStack.pop()
#             if len(idxStack) == 0:
#                 idxStack.append(i)
#             else:
#                 balancedSubstringStartIdx = idxStack[len(idxStack) - 1]
#                 currentLength = i - balancedSubstringStartIdx
#                 maxLength = max(maxLength, currentLength)

#     return maxLength



# Solution 4
# O(n^3) time | O(n) space - where n is the length of the input string
# def longestBalancedSubstring(string):
#     # Write your code here.
#     maxLength = 0

#     for i in range(len(string)):
#         for j in range(i + 2, len(string) + 1, 2):
#             if isBalanced(string[i:j]):
#                 currentLength = j - i
#                 maxLength = max(maxLength, currentLength)

#     return maxLength


# def isBalanced(string):
#     openParensStack = []

#     for char in string:
#         if char == "(":
#             openParensStack.append("(")
#         elif len(openParensStack) > 0:
#             openParensStack.pop()
#         else:
#             return False

#     return len(openParensStack) == 0
