# O(n) time | O(1) space - where n is the number of elements in the array
def majorityElement(array):
    # Write your code here.
    answer = 0

    for currentBit in range(32):
        currentBitValue = 1 << currentBit
        onesCount = 0

        for num in array:
            if (num & currentBitValue) != 0:
                onesCount += 1

        if onesCount > len(array) / 2:
            answer += currentBitValue
            
    return answer



# Solution 2
# O(n) time | O(1) space - where n is the number of elements in the array
# def majorityElement(array):
#     # Write your code here.
#     count = 0
#     answer = None

#     for value in array:
#         if count == 0:
#             answer = value

#         if value == answer:
#             count += 1
#         else:
#             count -= 1
            
#     return answer
