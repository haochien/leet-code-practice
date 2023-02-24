from typing import List
from math import ceil

class SearchInRotatedArray:
    """
    LeetCode Question Nr.33
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.


    Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Example 3:
    Input: nums = [1], target = 0
    Output: -1
    """
    @staticmethod
    def great_ans1(nums: List[int], target: int) -> int:


        return 

    @staticmethod
    def my_solution(nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            vl = nums[l]
            vr = nums[r]
            vm = nums[m]

            """
            exclude all "equal" case to simplify the logic check we are going to perform later on
            """
            if vl == target:
                return l

            if vr == target:
                return r

            if vm == target:
                return m

            """
            two type of array:
            1. when mid > left: (e.g. [4,5,6,7,0,1,2])
               a. we can always guarantee that target will be on the right side of mid if "target > mid"
               b. But if "target < mid": it can either be on the left of mid or right of mid.
                  So second check:
                  - target will definitely between left and mid if target > left
                  - target will definitely between mid and right if target < left
            
            2. when mid < left: (e.g. [8,1,2,3,4,5,6,7])
                a. we can always guarantee that target will be on the left side of mid if "target < mid"
                b. But if "target > mid": it can either be on the left of mid or right of mid.
                  So second check:
                  - target will definitely between mid and right if target < right
                  - target will definitely between left and mid if target > right
            """
            if vm > vl:
                if target > vm:
                    l = m + 1
                else:
                    if target > vl:
                        r = m - 1
                    else:
                        l = m + 1

            else:
                if target < vm:
                    r = m - 1
                else:
                    if target > vr:
                        r = m - 1
                    else:
                        l = m + 1
        return -1


    @staticmethod
    def my_solution1(nums: List[int], target: int) -> int:
        """
        wrong for [5,1,2,3,4] target 1
        output -1
        expect 1
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            vl = nums[l]
            vr = nums[r]
            vm = nums[m]

            if vl == target:
                return l

            if vr == target:
                return r

            if vm == target:
                return m

            if target > vm:
                l = m + 1
            else:
                if target > vl:
                    r = m - 1
                else:
                    l = m + 1
        return -1
        
 
