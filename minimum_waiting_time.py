# O(nlogn) time | O(1) space - where n is the number of queries 
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()

    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft
        
    return totalWaitingTime
