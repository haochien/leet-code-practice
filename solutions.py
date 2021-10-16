from typing import List


class Solution:
    def twoSum_my(self, nums: List[int], target: int) -> List[int]:
        """
        Question 1 - Leet Code Nr. 1
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Input: nums = [2,7,11,15], target = 9
        """
        results = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)-i):
                if nums[i] + nums[i+j] == target:
                    results.extend([i, i+j])
        return results


    def twoSum_ans1(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
        """
        results = {}
        for i, val in enumerate(nums):
            res = target - val

            if res in results:
                return [results[res], i]
            else:
                results[val] = i


    def twoSum_ans2(self, nums: List[int], target: int) -> List[int]:
        """
        In case nums has been already ascendingly sorted
        """
        right_index = len(nums) - 1
        for left_index in range(0, len(nums)-1):
            while left_index < right_index:
                sum_result = nums[left_index] + nums[right_index]
                if sum_result == target:
                    return [left_index, right_index]
                elif sum_result < target:
                    left_index += 1
                else:
                    right_index -= 1

