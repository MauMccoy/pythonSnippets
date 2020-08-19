#
#   This program demonstrates a optimized bubble sorting
#   method compared to a simple example.
#
#   It saves time by stopping the algorithm if the inner loop
#   didn'cause a swap

import os
import sys

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True

        if swap == False:
            break


# TEST CODE
arr = [45, 1, 76, 57, 23, 16, 87]

# Function call bubbleSort()
bubbleSort(arr)

# Prints sorted array
print ("Sorted Array:")
for i in range(len(arr)):
    print (arr[i]),
