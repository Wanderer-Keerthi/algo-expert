# O(low * high * n) time | O(low * high) space - where n is the number of measuring cups
def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    memoization = {}
    return canMeasureInRange(measuringCups, low, high, memoization)


def canMeasureInRange(measuringCups, low, high, memoization):
    memoizeKey = createHashableKey(low, high)
    if memoizeKey in memoization:
        return memoization[memoizeKey]

    if low <= 0 and high <= 0:
        return False

    canMeasure = False
    for cup in measuringCups:
        cupLow, cupHigh = cup
        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break

        newLow = max(0, low - cupLow)
        newHigh = max(0, high - cupHigh)
        canMeasure = canMeasureInRange(measuringCups, newLow, newHigh, memoization)
        if canMeasure:
            break

    memoization[memoizeKey] = canMeasure
    return canMeasure


def createHashableKey(low, high):
    return str(low) + ":" + str(high)
