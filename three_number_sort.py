# O(n) time | O(1) space - where n is the length of the array
def threeNumberSort(array, order):
    # Write your code here.
    firstValue = order[0]
    secondValue = order[1]

    # Keep track of the indices where the value are stored
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1
    
    while secondIdx <= thirdIdx:
        value = array[secondIdx]
        
        if value == firstValue:
            array[firstIdx], array[secondIdx] = array[secondIdx], array[firstIdx]
            firstIdx += 1
            secondIdx += 1
        elif value == secondValue:
            secondIdx += 1
        else:
            array[thirdIdx], array[secondIdx] = array[secondIdx], array[thirdIdx]
            thirdIdx -= 1

    return array



# Solution 2
# O(n) time | O(1) space - where n is the length of the array
# def threeNumberSort(array, order):
#     # Write your code here.
#     firstValue = order[0]
#     thirdValue = order[2]

#     firstIdx = 0
#     for idx in range(len(array)):
#         if array[idx] == firstValue:
#             array[firstIdx], array[idx] = array[idx], array[firstIdx]
#             firstIdx += 1

#     thirdIdx = len(array) - 1
#     for idx in range(len(array) - 1, -1 , -1):
#         if array[idx] == thirdValue:
#             array[thirdIdx], array[idx] = array[idx], array[thirdIdx]
#             thirdIdx -= 1

#     return array



# Solution 3
# O(n) time | O(1) space - where n is the length of the array
# def threeNumberSort(array, order):
#     # Write your code here.
#     valueCounts = [0, 0, 0]

#     for element in array:
#         orderIdx = order.index(element)
#         valueCounts[orderIdx] += 1

#     for i in range(3):
#         value = order[i]
#         count = valueCounts[i]

#         numElementsBefore = sum(valueCounts[:i])
#         for n in range(count):
#             currentIdx = numElementsBefore + n
#             array[currentIdx] = value

#     return array



# Solution 4
# def swap(i, j, array):
#     array[i], array[j] = array[j], array[i]

# def threeNumberSort(array, order):
#     # Write your code here.
#     first, second = 0, 0
#     third = len(array)-1
#     while second <= third:
#         if array[second] == order[0]:
#             swap(second, first, array)
#             first += 1
#             second += 1
#         elif array[second] == order[1]:
#             second += 1
#         else:
#             swap(second, third, array)
#             third -= 1
#     return array