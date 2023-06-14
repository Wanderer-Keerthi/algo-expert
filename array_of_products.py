# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
    # Write your code here.
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products



# Solution 2
# O(n) time | O(n) space - where n is the length of the input array
# def arrayOfProducts(array):
#     # Write your code here.
#     products = [1 for _ in range(len(array))]
#     leftProducts = [1 for _ in range(len(array))]
#     rightProducts = [1 for _ in range(len(array))]

#     leftRunningProduct = 1
#     for i in range(len(array)):
#         leftProducts[i] = leftRunningProduct
#         leftRunningProduct *= array[i]

#     rightRunningProduct = 1
#     for i in reversed(range(len(array))):
#         rightProducts[i] = rightRunningProduct
#         rightRunningProduct *= array[i]

#     for i in range(len(array)):
#         products[i] = leftProducts[i] * rightProducts[i]

#     return products



# Solution 3
# O(n^2) time | O(n) space - where n is the length of the input array
# def arrayOfProducts(array):
#     # Write your code here.
#     products = [1 for _ in range(len(array))]

#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if i != j:
#                 runningProduct *= array[j]
#         products[i] = runningProduct

#     return products
