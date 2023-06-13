HOME_TEAM_WON = 1

# O(n) time | O(k) space - where n is the number
# of competitions and k is the number of teams
def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam = ""
    score_board = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScoreBoard(winningTeam, 3, score_board)

        if score_board[winningTeam] > score_board[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam
            
def updateScoreBoard(team, points, score):
    if team not in score:
        score[team] = 0

    score[team] += points
