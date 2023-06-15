# O(n) time | O(1) space - where n is the number of cities
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    numberOfCities = len(distances)
    milesRemaining = 0

    indexOfStartingCityCandidate = 0
    milesRemainingAtStartingCityCandidate = 0

    for cityIdx in range(1, numberOfCities):
        distanceFromPreviousCity = distances[cityIdx - 1]
        fuelFromPreviousCity = fuel[cityIdx - 1]
        milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

        if milesRemaining < milesRemainingAtStartingCityCandidate:
            milesRemainingAtStartingCityCandidate = milesRemaining
            indexOfStartingCityCandidate = cityIdx

    return indexOfStartingCityCandidate



# Solution 2
# O(n^2) time | O(1) space - where n is the number of cities
# def validStartingCity(distances, fuel, mpg):
#     # Write your code here.
#     numberOfCities = len(distances)

#     for startCityIdx in range(numberOfCities):
#         milesRemaining = 0

#         for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):
#             if milesRemaining < 0:
#                 continue

#             currentCityIdx = currentCityIdx % numberOfCities

#             fuelFromCurrentCity = fuel[currentCityIdx]
#             distanceToNextCity = distances[currentCityIdx]
#             milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity

#         if milesRemaining >= 0:
#             return startCityIdx

#     # This line should never be reached if the inputs are correct
#     return -1
