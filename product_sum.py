# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# O(n) time | O(d) space - where n is the total number of elements in the array,
# including sub-elements, and d is the greatest depth of "special" arrays in the array
def productSum(array, multiplier=1):
    # Write your code here.
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier
