# O(w^2 * h) time | O(w) space - where w and h
# are the width and height of the input array
def waterfallStreams(array, source):
    # Write your code here.
    rowAbove = array[0][:]
    # We'll use -1 to represent water, since 1 is used for a block.
    rowAbove[source] = -1

    for row in range(1, len(array)):
        currentRow = array[row][:]

        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            hasWaterAbove = valueAbove < 0
            hasBlock = currentRow[idx] == 1

            if not hasWaterAbove:
                continue

            if not hasBlock:
                # If there is no block in the current column, move the water down.
                currentRow[idx] += valueAbove
                continue

            splitWater = valueAbove / 2

            # Move water right.
            rightIdx = idx
            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1: # if there is a block in the way
                    break
                if currentRow[rightIdx] != 1: # if there is no block below us
                    currentRow[rightIdx] += splitWater
                    break

            # Move water left.
            leftIdx = idx
            while leftIdx - 1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1: # if there is a block in the way
                    break
                if currentRow[leftIdx] != 1: # if there is no block below us
                    currentRow[leftIdx] += splitWater
                    break

        rowAbove = currentRow

    # Convert our negative values to positive percentages.
    finalPercentages = list(map(lambda num: num * -100, rowAbove))

    return finalPercentages
