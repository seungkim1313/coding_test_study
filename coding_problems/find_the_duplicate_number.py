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

def find_duplicate1(nums):
    answer = None

    answer, size = Counter(nums).most_common(1)[0]

    return answer

nums=[3,1,3,4,2]


def find_duplicate2(nums):
    tmp = set()
    for n in nums:
        if n in tmp:
            return n
        tmp.add(n)

import timeit

start = timeit.default_timer()
a = find_duplicate1(nums)
stop = timeit.default_timer()
print(stop-start)

start = timeit.default_timer()
a = find_duplicate2(nums)
stop = timeit.default_timer()
print(stop-start)