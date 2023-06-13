# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)


# Solution 2
# O(n) time | O(1) space - where n is the length of the array
# def isValidSubsequence(array, sequence):
#     # Write your code here.
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(array) and seqIdx < len(sequence):
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx += 1
#     return seqIdx == len(sequence)


# Solution 3
# def isValidSubsequence(array, sequence):
#     # Write your code here.
#     index = 0
#     for num in array:
#         if num == sequence[index]:
#             index += 1
#             if index == len(sequence):
#                 return True
#     return False   