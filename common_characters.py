# O(n * m) time | O(m) space - where n is the number of strings, and m is the
# length of the longest string
def commonCharacters(strings):
    # Write your code here.
    smallestString = getSmallestString(strings)
    potentialCommonCharacters = set(smallestString)

    for string in strings:
        removeNoneExistingCharacters(string, potentialCommonCharacters)

    return list(potentialCommonCharacters)


def getSmallestString(strings):
    smallestString = strings[0]
    for string in strings:
        if len(string) < len(smallestString):
            smallestString = string

    return smallestString


def removeNoneExistingCharacters(string, potentialCommonCharacters):
    uniqueStringCharacters = set(string)
    
    for character in list(potentialCommonCharacters):
        if character not in uniqueStringCharacters:
            potentialCommonCharacters.remove(character)



# Solution 2
# O(n * m) time | O(c) space - where n is the number of strings, m is the
# length of the longest string, and c is the number of unique characters across
# all strings
# def commonCharacters(strings):
#     # Write your code here.
#     characterCounts = {}
#     for string in strings:
#         uniqueStringCharacters = set(string)
#         for character in uniqueStringCharacters:
#             if character not in characterCounts:
#                 characterCounts[character] = 0
#             characterCounts[character] += 1

#     finalCharacters = []
#     for character, count in characterCounts.items():
#         if count == len(strings):
#             finalCharacters.append(character)

#     return finalCharacters
