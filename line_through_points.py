# O(n^2) time | O(n) space - where n is the number of points
def lineThroughPoints(points):
    # Write your code here.
    maxNumberOfPointsOnLine = 1

    for idx1, p1 in enumerate(points):
        slopes = {}
        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            rise, run = getSlopeOfLineBetweenPoints(p1, p2)
            slopeKey = createHashableKeyForRational(rise, run)
            if slopeKey not in slopes:
                slopes[slopeKey] = 1

            slopes[slopeKey] += 1

        maxNumberOfPointsOnLine = max(maxNumberOfPointsOnLine, max(slopes.values(), default=0))

    return maxNumberOfPointsOnLine


def getSlopeOfLineBetweenPoints(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    slope = [1, 0] # slope of a vertical line

    if p1x != p2x: # if line is not vertical
        xDiff = p1x - p2x
        yDiff = p1y - p2y
        gcd = getGreatestCommonDivisor(abs(xDiff), abs(yDiff))
        xDiff = xDiff // gcd
        yDiff = yDiff // gcd
        if xDiff < 0:
            xDiff *= -1
            yDiff *= -1

        slope = [yDiff, xDiff]

    return slope


def createHashableKeyForRational(numerator, denominator):
    return str(numerator) + ":" + str(denominator)


def getGreatestCommonDivisor(num1, num2):
    a = num1
    b = num2
    while True:
        if a == 0:
            return b
        if b == 0:
            return a

        a, b = b, a % b
