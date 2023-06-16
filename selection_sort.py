# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):
    # Write your code here.
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
