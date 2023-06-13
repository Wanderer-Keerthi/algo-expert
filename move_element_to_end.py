# O(n) time | O(1) space - where n is the length of the array
def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array



#  Solution 2
# def moveElementToEnd(array, toMove):
#     # Write your code here.
#     cnt = 0
#     for i in range(0, len(array)):
#         if array[i] != toMove:
#             array[cnt] = array[i]
#             cnt += 1

#     while cnt < len(array):
#         array[cnt] = toMove
#         cnt += 1
    
#     return array