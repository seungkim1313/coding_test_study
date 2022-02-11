"""
LeetCode Problem - Medium
567. Permutation in String

Given two strings 's1' and 's2', return 'true' if 's2' contains a permutation of s1,
or 'false' otherwise. In other words, return 'true' if one of s1's permutation is the substring of s2.

example #1
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

example #2
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""


'''
from itertools import permutations

## It works but has time limit problem 
def permutation_in_string(s1, s2):
    for p in permutations(s1):
        _tmp = ''.join(p)
        if _tmp in s2:
            return True
    return False
'''

from collections import Counter

def permutation_in_string(s1, s2):
    
    count_s1 = Counter(s1)
    for i, s in enumerate(s2):
        if s in s1:
            count_sub = Counter(s2[i:i+len(s1)])
            if count_s1 == count_sub:
                return True
    return False


s1 = "ab"
s2 = "eidbaooo"
print(permutation_in_string(s1, s2))