# O(t - s) time | O(t - s) space - where t is the target, and s is the
# starting hand
def blackjackProbability(target, startingHand):
    # Write your code here.
    memo = {}
    return round(calculateProbability(startingHand, target, memo), 3)


def calculateProbability(currentHand, target, memo):
    if currentHand in memo:
        return memo[currentHand]
    if currentHand > target:
        return 1
    if currentHand + 4 >= target:
        return 0

    totalProbability = 0
    for drawnCard in range(1, 11):
        totalProbability += 0.1 * calculateProbability(currentHand + drawnCard, target, memo)

    memo[currentHand] = totalProbability
    return totalProbability
