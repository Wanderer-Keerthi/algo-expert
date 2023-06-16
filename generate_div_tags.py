# O((2n)!/((n!((n + 1)!)))) time | O((2n)!/((n!((n + 1)!)))) space -
# where n is the input number
def generateDivTags(numberOfTags):
    # Write your code here.
    matchedDivTags = []
    generateDivTagsFromPrefix(numberOfTags, numberOfTags, "", matchedDivTags)
    return matchedDivTags


def generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagsNeeded - 1, closingTagsNeeded, newPrefix, result)

    if openingTagsNeeded < closingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded - 1, newPrefix, result)

    if closingTagsNeeded == 0:
        result.append(prefix)
