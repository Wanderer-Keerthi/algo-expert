# O(n^2) time | O(n) space - where n is the number of points
def countSquares(points):
    # Write your code here.
    pointsSet = set()
    for point in points:
        pointsSet.add(pointToString(point))

    count = 0
    for pointA in points:
        for pointB in points:
            if pointA == pointB:
                continue

            midpoint = [(pointA[0] + pointB[0]) / 2, (pointA[1] + pointB[1]) / 2]
            xDistanceFromMid = pointA[0] - midpoint[0]
            yDistanceFromMid = pointA[1] - midpoint[1]

            pointC = [midpoint[0] + yDistanceFromMid, midpoint[1] - xDistanceFromMid]
            pointD = [midpoint[0] - yDistanceFromMid, midpoint[1] + xDistanceFromMid]

            if pointToString(pointC) in pointsSet and pointToString(pointD) in pointsSet:
                count += 1

    return count / 4


def pointToString(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(coordinate) for coordinate in point]
        
    return ",".join([str(coordinate) for coordinate in point])
