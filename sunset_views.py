# O(n) time | O(n) space - where n is the length of the input array
def sunsetViews(buildings, direction):
    # Write your code here.
    candidateBuildings = []

    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    step = 1 if direction == "EAST" else -1 

    idx = startIdx
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <=buildingHeight:
            candidateBuildings.pop()
            
        candidateBuildings.append(idx)

        idx += step

    if direction == "WEST":
        return candidateBuildings[::-1]
        
    return candidateBuildings



# Solution 2
# O(n) time | O(n) space - where n is the length of the input array
# def sunsetViews(buildings, direction):
#     # Write your code here.
#     buildingsWithSunsetViews = []

#     startIdx = 0 if direction == "WEST" else len(buildings) - 1
#     step = 1 if direction == "WEST" else -1 

#     idx = startIdx
#     runningMaxHeight = 0
#     while idx >= 0 and idx < len(buildings):
#         buildingHeight = buildings[idx]

#         if buildingHeight > runningMaxHeight:
#             buildingsWithSunsetViews.append(idx)

#         runningMaxHeight = max(runningMaxHeight, buildingHeight)

#         idx += step

#     if direction == "EAST":
#         return buildingsWithSunsetViews[::-1]
        
#     return buildingsWithSunsetViews
