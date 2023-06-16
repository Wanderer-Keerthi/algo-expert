# O(n + m) time | O(c) space - where n is the number of characters, m is 
# the length of the document, and c is the number of unique characters in the characters string
def generateDocument(characters, document):
    # Write your code here.
    characterCounts = {}
    
    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1

    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1
    
    return True



# Solution 2
# O(c * (n + m)) time | O(c) space - where n is the number of characters, m is 
# the length of the document, and c is the number of unique characters in the document
# def generateDocument(characters, document):
#     # Write your code here.
#     alreadyCounted = set()

#     for character in document:
#         if character in alreadyCounted:
#             continue
        
#         documentFrequency = countCharacterFrequency(character, document)
#         charactersFrequency = countCharacterFrequency(character, characters)
#         if documentFrequency > charactersFrequency:
#             return False

#         alreadyCounted.add(character)
            
#     return True


# def countCharacterFrequency(character, target):
#     frequency = 0
#     for char in target:
#         if char ==  character:
#             frequency += 1

#     return frequency



# Solution 3
# O(m * (n + m)) time | O(1) space - where n is the number
# of characters and m is the length of the document
# def generateDocument(characters, document):
#     # Write your code here.
#     for character in document:
#         documentFrequency = countCharacterFrequency(character, document)
#         charactersFrequency = countCharacterFrequency(character, characters)
#         if documentFrequency > charactersFrequency:
#             return False
            
#     return True


# def countCharacterFrequency(character, target):
#     frequency = 0
#     for char in target:
#         if char ==  character:
#             frequency += 1

#     return frequency
