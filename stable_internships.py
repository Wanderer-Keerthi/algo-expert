# O(n^2) time | O(n^2) space - where n is the number of interns and teams
def stableInternships(interns, teams):
    # Write your code here.
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0] * len(interns)

    teamMaps = []
    for team in teams:
        rank = {}
        for i, internNum in enumerate(team):
            rank[internNum] = i
        teamMaps.append(rank)

    while len(freeInterns) > 0:
        internNum = freeInterns.pop()

        intern = interns[internNum]
        teamPreference = intern[currentInternChoices[internNum]]
        currentInternChoices[internNum] += 1

        if teamPreference not in chosenInterns:
            chosenInterns[teamPreference] = internNum
            continue

        previousIntern = chosenInterns[teamPreference]
        previousInternRank = teamMaps[teamPreference][previousIntern]
        currentInternRank = teamMaps[teamPreference][internNum]

        if currentInternRank < previousInternRank:
            freeInterns.append(previousIntern)
            chosenInterns[teamPreference] = internNum
        else:
            freeInterns.append(internNum)

    matches = [[internNum, teamNum] for teamNum, internNum in chosenInterns.items()]
    return matches
