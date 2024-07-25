# count inversions problem
# ṃodified merge sort algorithm



from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n):
    temp = [0] * n
    return divide(arr, temp, 0, n - 1)

def divide(arr, temp, left, right):
    invcount = 0
    if left < right:
        mid = (left + right) // 2
        # Count inversions in the left half
        invcount += divide(arr, temp, left, mid)
        # Count inversions in the right half
        invcount += divide(arr, temp, mid + 1, right)
        # Count inversions that span across the two halves
        invcount += merge(arr, temp, left, mid, right)
    return invcount

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    invcount = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            invcount += (mid - i + 1)  # Count the inversions here
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return invcount

# Taking input using fast I/O
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main
arr, n = takeInput()
print(getInversions(arr, n))
