#
#   This program demonstrates a simple bubble sorting
#   method.

import os
import sys

# Bubble sorting function
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# TEST CODE
arr = [45, 1, 76, 57, 23, 16, 87]

# Function call bubbleSort()
bubbleSort(arr)

# Prints sorted array
print ("Sorted Array:")
for i in range(len(arr)):
    print (arr[i]),
