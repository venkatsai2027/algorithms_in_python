# this is for 1=based indexing
# Code and algorithm for Repeat and missing numbers

def repeatedNumber(A):
    # Phase 1: Finding the intersection point of the two runners.
    slow = A[0]
    fast = A[0]
    while True:
        slow = A[slow-1]
        fast = A[A[fast-1]-1]
        if slow == fast:
            break
    
    # Phase 2: Finding the entrance to the cycle.
    slow = A[0]
    while slow != fast:
        slow = A[slow-1]
        fast = A[fast-1]
    
    # The duplicate number
    duplicate = slow
    
    # Calculate the sum of the first n natural numbers
    n = len(A)
    total_sum = n * (n + 1) // 2
    
    # Calculate the sum of the elements in the array
    array_sum = sum(A)
    
    # The missing number
    missing = total_sum - (array_sum - duplicate)
    
    return [duplicate, missing]

# Test case
print(repeatedNumber([3, 1, 4, 5, 3]))
# print(repeatedNumber([1,3,4,2,2]))