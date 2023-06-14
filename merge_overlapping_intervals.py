# O(nlog(n)) time | O(n) space - where n is the length of the input array
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
        
    return mergedIntervals
