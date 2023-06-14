# O(nm) time | O(nm) space
def longestCommonSubsequence(str1, str2):
    # Write your code here.
    dp_array = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            else:
                dp_array[i][j] = max(dp_array[i][j - 1], dp_array[i - 1][j])
    return buildSequence(dp_array, str1)


def buildSequence(array, string):
    sequence = []
    m = len(array) - 1
    n = len(array[0]) - 1
    
    while m != 0 and n != 0:
        if array[m][n] == array[m - 1][n]:
            m -= 1
        elif array[m][n] == array[m][n - 1]:
            n -= 1
        else:
            sequence.append(string[n - 1])
            m -= 1
            n -= 1
    return list(reversed(sequence))


# Solution 2
# O(nm) time | O(nm) space
# def longestCommonSubsequence(str1, str2):
#     # Write your code here.
#     lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             if str2[i - 1] == str1[j - 1]:
#                 lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
#             else:
#                 if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
#                     lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
#                 else:
#                     lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]
#     return buildSequence(lcs)


# def buildSequence(lcs):
#     sequence = []
#     i = len(lcs) - 1
#     j = len(lcs[0]) - 1
    
#     while i != 0 and j != 0:
#         currentEntry = lcs[i][j]
#         if currentEntry[0] is not None:
#             sequence.append(currentEntry[0])
#         i = currentEntry[2]
#         j = currentEntry[3]
#     return list(reversed(sequence))



# Solution 3
# O(nm*min(n, m)) time | O((min(n, m))^2) space
# def longestCommonSubsequence(str1, str2):
#     # Write your code here.
#     small = str1 if len(str1) < len(str2) else str2
#     big = str1 if len(str1) >= len(str2) else str2
#     evenLcs = [[] for x in range(len(small) + 1)]
#     oddLcs = [[] for x in range(len(small) + 1)]
#     for i in range(1, len(big) + 1):
#         if i % 2 == 1:
#             currentLcs = oddLcs
#             previousLcs = evenLcs
#         else:
#             currentLcs = evenLcs
#             previousLcs = oddLcs
#         for j in range(1, len(small) + 1):
#             if big[i - 1] == small[j - 1]:
#                 currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]
#             else:
#                 currentLcs[j] = max(previousLcs[j], currentLcs[j - 1], key=len)
#     return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]



# Solution 4
# O(nm*min(n, m)) time | O(nm*min(n, m)) space
# def longestCommonSubsequence(str1, str2):
#     # Write your code here.
#     lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             if str2[i - 1] == str1[j - 1]:
#                 lcs[i][j] = lcs[i - 1][j - 1] + [str2[i - 1]]
#             else:
#                 lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)
#     return lcs[-1][-1]
