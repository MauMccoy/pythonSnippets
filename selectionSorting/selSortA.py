# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This is a selection sort snippet for simple tasks in python...                #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
arr = [11 ,69 ,37 ,58 ,29 ,112]

# Read through all the elements of the array
for i in range(len(arr)):

    # Find the minimum element in the unsorted array
    min_element = i
    for j in range(i+1, len(arr)):
        if arr[min_element] > arr[j]:
            min_element = j

    # Swap the found minimum element with the first element
    arr[i], arr[min_element] = arr[min_element], arr[i]

# print test
print ("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i]),
