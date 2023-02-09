from typing import List

class Subsets:
    """
    LeetCode Question Nr.78
    https://leetcode.com/problems/subsets/
    
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    A subset of an array is a selection of elements (possibly none) of the array.

    The solution set must not contain duplicate subsets. Return the solution in any order.

    Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Example 2:
    Input: nums = [0]
    Output: [[],[0]]
    """

    @staticmethod
    def great_ans1(nums: List[int]) -> List[List[int]]:
        """
        technique: backtracking
        Time: O(n)
        Memory: O(n)
        https://www.youtube.com/watch?v=REOH22Xwdkk


                                            0
                            1 /                           \ []
                          [1]                             []
                  2 /              \ []           2 /            \ [] 
                [1,2]             [1]            [2]             []
            3 /      \ []    3 /      \ []   3 /     \ []    3 /    \ [] 
        [1,2,3]    [1,2]    [1,3]    [1]    [2,3]    [2]    [3]      []
            

        """

        res = []

        subset = []
        def dfs(i):
            if i > len(nums)-1:
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        
        
