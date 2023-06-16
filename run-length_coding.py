# O(n) time | O(n) space - where n is the length of the input string
def runLengthEncoding(string):
    # Write your code here.
    # The input string is guaranteed to be non-empty,
    # so our first run will be of at least length 1.
    encodedStringCharacters = []
    currentRunLength = 1

    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]

        if currentCharacter != previousCharacter or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)
            currentRunLength = 0

        currentRunLength += 1

    # Handle the last run.
    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string)-1])
    
    return "".join(encodedStringCharacters)
