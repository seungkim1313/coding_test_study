"""
LeetCode Problem - Medium
560. Subarray Sum Equals K

Given an array of integers 'nums' and an integer 'k', return the total number of continuous subarrays whose sum equals to k

example #1
input: nums = [1, 1, 1], k = 2
outpus: 2

example #2
input: nums = [1, 2, 3], k = 3
output: 2
"""

def subarraySum(nums, k):
    
    answer = 0
    _sum = 0
        
    _map = {0: 1}
        
    for i in nums:
        _sum += i
            
        if _map.get(_sum-k):
            answer += _map[_sum-k]
                
        if _map.get(_sum):
            _map[_sum] += 1
        else:
            _map[_sum] = 1
        
    return answer

nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))