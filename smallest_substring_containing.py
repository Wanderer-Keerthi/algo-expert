# O(b + s) time | O(b + s) space - where b is the length of the big 
# input string and s is the length of the small input string
def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    targetCharCounts = getCharCounts(smallString)
    substringBounds = getSubstringBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, substringBounds)


def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts


def getSubstringBounds(string, targetCharCounts):
    substringBounds = [0, float("inf")]
    substringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    numUniqueCharsDone = 0
    leftIdx = 0
    rightIdx = 0
    # Move the rightIdx to the right in the string until you've counted
    # all of the target characters enough times.
    while rightIdx < len(string):
        rightChar = string[rightIdx]
        if rightChar not in targetCharCounts:
            rightIdx += 1
            continue
        increaseCharCount(rightChar, substringCharCounts)
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharsDone += 1
        # Move the leftIdx to the right in the string until you no longer
        # have enough of the target characters in between the leftIdx and
        # the rightIdx. Update the substringBounds accordingly.
        while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx:
            substringBounds = getCloserBounds(leftIdx, rightIdx, substringBounds[0], substringBounds[1])
            leftChar = string[leftIdx]
            if leftChar not in targetCharCounts:
                leftIdx += 1
                continue
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharsDone -= 1
            decreaseCharCount(leftChar, substringCharCounts)
            leftIdx += 1
        rightIdx += 1
    return substringBounds


def getCloserBounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]


def getStringFromBounds(string, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""
    return string[start : end + 1]


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1


def decreaseCharCount(char, charCounts):
    charCounts[char] -= 1



# Solution 2
# no_of_chars = 256
# def smallestSubstringContaining(bigString, smallString):
#     # Write your code here.
#     bigString_len = len(bigString)
#     smallString_len = len(smallString)

#     if bigString_len < smallString_len:
#         return ""

#     bigString_arr = [0] * no_of_chars
#     smallString_arr = [0] * no_of_chars

#     for idx in range(smallString_len):
#         smallString_arr[ord(smallString[idx])] += 1

#     start, start_idx, min_char = 0, -1, float('inf')
#     count = 0

#     for char_idx in range(bigString_len):
#         bigString_arr[ord(bigString[char_idx])] += 1

#         if smallString_arr[ord(bigString[char_idx])] != 0 and bigString_arr[ord(bigString[char_idx])] <= smallString_arr[ord(bigString[char_idx])]:
#             count += 1

#         if count == smallString_len:

#             while bigString_arr[ord(bigString[start])] > smallString_arr[ord(bigString[start])] or smallString_arr[ord(bigString[start])] == 0:
                
#                 if bigString_arr[ord(bigString[start])] > smallString_arr[ord(bigString[start])]:
#                     bigString_arr[ord(bigString[start])] -= 1
    
#                 start += 1

#             window_char = char_idx - start + 1
#             if window_char < min_char:
#                 min_char = window_char
#                 start_idx = start

#     if start_idx == -1:
#         return ""

#     return bigString[start_idx: start_idx + min_char]
