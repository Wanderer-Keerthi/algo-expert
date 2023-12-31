# O(d * (n + b)) time | O(n + b) space - where n is the length of the input array,
# d is the max  number of digits, and b is the base of the numbering system used
def radixSort(array):
    # Write your code here.
    if len(array) == 0:
        return array

    maxNumber = max(array)
    
    digit = 0
    while maxNumber / 10 ** digit > 0:
        countingSort(array, digit)
        digit += 1

    return array

def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countedArray = [0] * 10

    digitColumn = 10 ** digit
    for num in array:
        countIndex = (num // digitColumn) % 10
        countedArray[countIndex] += 1

    for idx in range(1, 10):
        countedArray[idx] += countedArray[idx - 1]

    for idx in range(len(array)-1, -1, -1):
        countIndex = (array[idx] // digitColumn) % 10
        countedArray[countIndex] -= 1
        sortedIndex = countedArray[countIndex]
        sortedArray[sortedIndex] = array[idx]

    for idx in range(len(array)):
        array[idx] = sortedArray[idx]
