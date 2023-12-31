# O(n) time | O(n) space - where n is the length of the string
def reverseWordsInString(string):
    # Write your code here.
    characters = [char for char in string]
    reverseListRange(characters, 0, len(characters) - 1)
    
    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1

        reverseListRange(characters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1

    return "".join(characters)


def reverseListRange(list, start, end):
    while start < end:
        list[start] , list[end] = list[end] , list[start]
        start += 1
        end -= 1



# Solution 2
# O(n) time | O(n) space - where n is the length of the string
# def reverseWordsInString(string):
#     # Write your code here.
#     words = []
#     startOfWord = 0
#     for idx in range(len(string)):
#         character = string[idx]

#         if character == " ":
#             words.append(string[startOfWord:idx])
#             startOfWord = idx
#         elif string[startOfWord] == " ":
#             words.append(" ")
#             startOfWord = idx

#     words.append(string[startOfWord:])

#     reverseList(words)
#     return "".join(words)


# def reverseList(list):
#     start, end = 0, len(list) - 1
#     while start < end:
#         list[start], list[end] = list[end], list[start]
#         start += 1
#         end -= 1
