#
#   This program demonstrates recursive bubble sorting
#

import os
import sys

def bubble_sort(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1] < num:
                arr[i] = arr[i+1]
                arr[i+1] = num
                bubble_sort(arr)
        except IndexError:
            pass
    return arr


# TEST CODE
arr = [45, 1, 76, 57, 23, 16, 87]

# Function call bubbleSort()
bubble_sort(arr)

# Prints sorted array
print ("Sorted Array:")
for i in range(len(arr)):
    print (arr[i]),
