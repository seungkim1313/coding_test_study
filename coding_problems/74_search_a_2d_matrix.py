"""
LEETCODE PROBLEM - MEDIUM
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""

import numpy as np

def searchMatrix1(matrix, target):
    return np.isin(target, np.matrix(matrix))


def searchMatrix2(matrix, target):
    x = 0
    y = int(len(matrix[0])-1)

    while x < len(matrix) and y >= 0:
        if target == matrix[x][y]:
            return True
        elif target < matrix[x][y]:
            y -= 1
        else:
            x += 1
    return False


def searchMatrix3(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    
    low = 0
    high = int((m*n)-1)

    while low <= high:
        mid = int((low+high) / 2)
        a = int(mid/n)
        b = int(mid%n)
        if matrix[a][b] == target:
            return True
        elif matrix[a][b] < target:
            low = mid+1
        else:
            high = mid-1
    return False


def searchMatrix4(matrix, target):
    row_low = 0
    row_high = len(matrix)-1
    while row_low <= row_high:
        row_mid = int((row_low+row_high) / 2)
        if matrix[row_mid][0] > target:
            row_high = row_mid-1
        elif matrix[row_mid][-1] < target:
            row_low = row_mid+1
        else:
            col_low = 0
            col_high = len(matrix[0])-1
            while col_low <= col_high:
                col_mid = int((col_low+col_high)/2)
                if matrix[row_mid][col_mid] == target:
                    return True
                if matrix[row_mid][col_mid] > target:
                    col_high = col_mid - 1
                else:
                    col_low = col_mid + 1
            return False


input_1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
input_2 = 13

output = searchMatrix3(input_1, input_2)

print(output) 