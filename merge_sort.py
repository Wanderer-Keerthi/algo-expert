# Best: O(nlog(n)) time | O(n) space
# Average: O(nlog(n)) time | O(n) space
# Worst: O(nlog(n)) time | O(n) space
def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array
    auxiliaryArray = array[:]
    mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
    return array


def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    k = startIdx
    i = startIdx
    j = middleIdx + 1
    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1



# Solution 2
# Best: O(nlog(n)) time | O(nlog(n)) space
# Average: O(nlog(n)) time | O(nlog(n)) space
# Worst: O(nlog(n)) time | O(nlog(n)) space
# def mergeSort(array):
#     # Write your code here.
#     if len(array) == 1:
#         return array
#     middleIdx = len(array) // 2
#     leftHalf = array[:middleIdx]
#     rightHalf = array[middleIdx:]
#     return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


# def mergeSortedArrays(leftHalf, rightHalf):
#     sortedArray = [None] * (len(leftHalf) + len(rightHalf))
#     k = i = j = 0
#     while i < len(leftHalf) and j < len(rightHalf):
#         if leftHalf[i] <= rightHalf[j]:
#             sortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             sortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1
#     while i < len(leftHalf):
#         sortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1
#     while j < len(rightHalf):
#         sortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1
#     return sortedArray



# Solution 3
# def merge(arr, dummy, low, mid, high):
#     k, i, j = low, low, mid + 1

#     while i <= mid and j <= high:
#         if arr[i] <= arr[j]:
#             dummy[k] = arr[i]
#             i += 1
#         else:
#             dummy[k] = arr[j]
#             j += 1
#         k += 1

#     while i <= mid:
#         dummy[k] = arr[i]
#         i += 1
#         k += 1

#     for i in range(low, high + 1):
#         arr[i] = dummy[i]

# def divide(arr, dummy, low, high):
#     if low == high:
#         return

#     mid = (low + high) // 2

#     divide(arr, dummy, low, mid)
#     divide(arr, dummy, mid + 1, high)

#     merge(arr, dummy, low, mid, high)

# def mergeSort(array):
#     # Write your code here.
#     low = 0
#     high = len(array) - 1
#     result = array.copy()
#     divide(array, result, low, high)
#     return array
