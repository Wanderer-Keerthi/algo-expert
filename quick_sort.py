# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space
def quickSort(array):
    # Write your code here.
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(array, leftIdx, rightIdx)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(array, pivotIdx, rightIdx)
    leftSubArraySmaller = rightIdx - 1 - startIdx > endIdx - (rightIdx + 1)
    if leftSubArraySmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
