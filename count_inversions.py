# O(nlogn) time | O(n) space - where n is the length of the array
def countInversions(array):
	return countInversionsHelper(array, 0, len(array))


def countInversionsHelper(array, start, end):
	if end - start <= 1:
		return 0
	
	middle = start + (end - start) // 2
	leftInversions = countInversionsHelper(array, start, middle)
	rightInversions = countInversionsHelper(array, middle, end)
	mergedArrayInversions = mergeSortAndCountInversions(array, start, middle, end)
	return leftInversions + rightInversions + mergedArrayInversions


def mergeSortAndCountInversions(array, start, middle, end):
	sortedArray = []
	left = start
	right = middle
	inversions = 0
		
	while left < middle and right < end:
		if array[left] <= array[right]:
			sortedArray.append(array[left])
			left += 1
		else:
			inversions += middle - left # All the numbers which are not yet sorted in the left array need to be inverted
			sortedArray.append(array[right])
			right += 1
		
	sortedArray += array[left:middle] + array[right:end]
	for idx, num in enumerate(sortedArray):
		array[start + idx] = num

	return inversions



# Solution 2
# Brute Force Approach | Time Complexity: O(n^2)
# def countInversions(array):
#     # Write your code here.
#     inversions = 0
#     for i in range(len(array)-1):
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 inversions += 1
#     return inversions
