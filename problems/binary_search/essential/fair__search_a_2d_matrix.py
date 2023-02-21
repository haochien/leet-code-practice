from typing import List

class Search2DMatrix:
    """
    LeetCode Question Nr.74
    https://leetcode.com/problems/search-a-2d-matrix/

    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

    Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false
    """



    @staticmethod
    def my_solution(matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix)-1
        
        while d - u > 1:
            mid = (u + d) // 2

            if matrix[mid][0] > target:
                d = mid
            elif matrix[mid][0] < target:
                u = mid
            else:
                return True

        target_i = d if target >= matrix[d][0] else u
        
        # this part is O(n) and can be improved by the codes below 
        # if target in matrix[target_i]:
        #     return True
        
        target_row = matrix[target_i]
        l, r = 0, len(target_row) - 1
        while r >= l:
            mid = (l + r) // 2
            if target_row[mid] > target:
                r -= 1
            elif target_row[mid] < target:
                l += 1
            else:
                return True

        return False
            

 
