# O(n) time | O(1) space
def isPalindrome(string):
    # Write your code here.
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True



# Solution 2
# O(n) time | O(n) space
# def isPalindrome(string, i=0):
#     # Write your code here.
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)



# Solution 3
# O(n) time | O(n) space
# def isPalindrome(string):
#     # Write your code here.
#     reversedChars = []
#     for i in reversed(range(len(string))):
#         reversedChars.append(string[i])
#     return string == "".join(reversedChars)



# Solution 4
# O(n^2) time | O(n) space
# def isPalindrome(string):
#     # Write your code here.
#     reversedString = ""
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString