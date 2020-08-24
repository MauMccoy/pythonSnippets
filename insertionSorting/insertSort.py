#
#   This program demonstrates insertion Sorting
#

import sys
import os

# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# TEST CODE
arr = [45, 1, 76, 57, 23, 16, 87]

# Function call bubbleSort()
insertionSort(arr)

# Prints sorted array
print ("Sorted Array:")
for i in range(len(arr)):
    print (arr[i]),
