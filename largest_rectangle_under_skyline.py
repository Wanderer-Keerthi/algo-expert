# O(n) time | O(n) space - where n is the number of buildings
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    pillarIndices = []
    maxArea = 0

    for idx, height in enumerate(buildings + [0]):
        while len(pillarIndices) != 0 and buildings[pillarIndices[len(pillarIndices) - 1]] >= height:
            pillarHeight = buildings[pillarIndices.pop()]
            width = idx if len(pillarIndices) == 0 else idx - pillarIndices[len(pillarIndices) - 1] - 1
            maxArea = max(width * pillarHeight, maxArea)

        pillarIndices.append(idx)
        
    return maxArea



# Solution 2
# O(n^2) time | O(1) space - where n is the number of buildings
# def largestRectangleUnderSkyline(buildings):
#     # Write your code here.
#     maxArea = 0
#     for pillarIdx in range(len(buildings)):
#         currentHeight = buildings[pillarIdx]

#         furthestLeft = pillarIdx
#         while furthestLeft > 0 and buildings[furthestLeft - 1] >= currentHeight:
#             furthestLeft -= 1

#         furthestRight = pillarIdx
#         while furthestRight < len(buildings) - 1 and buildings[furthestRight + 1] >= currentHeight:
#             furthestRight += 1

#         areaWithCurrentBuilding = (furthestRight - furthestLeft + 1) * currentHeight
#         maxArea = max(areaWithCurrentBuilding, maxArea)

#     return maxArea
