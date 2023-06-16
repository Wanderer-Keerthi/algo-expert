# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(caesarCipherEncryptorHelper(letter, newKey))
    return "".join(newLetters)

def caesarCipherEncryptorHelper(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# Soltion 2
# O(n) time | O(n) space
# def caesarCipherEncryptor(string, key):
#     # Write your code here.
#     newLetters = []
#     newKey = key % 26
#     alphabet = list("abcdefghijklmnopqrstuvwxyz")
#     for letter in string:
#         newLetters.append(getNewLetter(letter, newKey, alphabet))
#     return "".join(newLetters)


# def getNewLetter(letter, key, alphabet):
#     newLetterCode = alphabet.index(letter) + key
#     return alphabet[newLetterCode % 26]
