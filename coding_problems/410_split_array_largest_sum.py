"""
LEETCODE PROBLEM - HARD
410. Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""

# Dynamic Programming Approach



# Binary Search Approach (Optimal Solution)
def splitArray(nums, m):
    low = max(nums)
    high = sum(nums)
    print(low)
    print(high)
    
    answer = None
    
    while low <= high:
        mid = int((low+high) / 2)

        curr_sum = 0
        split_req = 0

        for n in nums:
            if curr_sum + n <= mid:
                curr_sum += n
            else:
                curr_sum = n
                split_req += 1
        split_req += 1

        if split_req <= m:
            high = mid - 1
            answer = mid
        else:
            low = mid + 1
    
    print(answer)


nums = [1,2,3,4,5]
m = 2

splitArray(nums, m)
