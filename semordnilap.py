# O(n * m) time | O(n * m) space - where n is the number of words and
# m is the length of the longest word
def semordnilap(words):
    # Write your code here.
    wordsSet = set(words)
    semordnilapPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            semordnilapPairs.append([word, reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)

    return semordnilapPairs
