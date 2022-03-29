"""
LeetCode Problem - MEDIUM
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2
"""
from collections import Counter

def find_duplicate(nums):
    answer = None

    answer, size = Counter(nums).most_common(1)[0]

    return answer

nums=[3,1,3,4,2]

a = find_duplicate(nums)
print(a)