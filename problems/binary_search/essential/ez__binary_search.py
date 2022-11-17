from typing import List

class BinarySearch:
    """
    LeetCode Question Nr.704
    https://leetcode.com/problems/binary-search/

    Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.

    Input: nums = [-1,0,3,5,9,12], target = 9    Output: 4
    Explanation: 9 exists in nums and its index is 4

    Input: nums = [-1,0,3,5,9,12], target = 2    Output: -1
    Explanation: 2 does not exist in nums so return -1
    """

    @staticmethod
    def great_ans1(nums: List[int], target: int) -> int:
        """
        technique: binary search
        Time: O(logn)
        Memory: O(1)
        https://www.youtube.com/watch?v=s4DPM8ct1pI
        """
        l, r = 0, len(nums) - 1

        while l <= r:  # needs to be smaller and equal to for the case such as [1]
            mid = (l + r) // 2  # in language like C, to prevent overfloat (when l is close to 2^31): mid = l + (r-l)//2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1   


    @staticmethod
    def my_solution(nums: List[int], target: int) -> int:
        """
        tech use : binary search
        """
        target_index = 0
        
        while len(nums) > 1:
            split_index = int(len(nums)/2)
            
            if target < nums[split_index]:
                nums = nums[:split_index]
                target_index += 0 
            elif target > nums[split_index]:
                nums = nums[split_index:]
                target_index += split_index
            else:
                target_index += split_index
                return target_index
        
        return target_index if nums[0] == target else -1
            

 
