from typing import List

class TwoSum:
    """
    LeetCode Question Nr.1
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9  Output: [0,1]
    Input: nums = [3,2,4], target = 6  Output: [1,2]
    Input: nums = [3,3], target = 6  Output: [0,1]
    """

    @staticmethod
    def great_ans1(nums: List[int], target: int) -> List[int]:
        """
        technique: Hash Map
        Time: O(n) 
        Memory: O(n) : from hash map
        Expination Sources:
        https://youtu.be/KLlXCFG5TnA
        https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
        """
        prev_map = {}  # val : index
        for i, val in enumerate(nums):
            res = target - val

            if res in prev_map:
                return [prev_map[res], i]  # return prev index and current index
            
            prev_map[val] = i  # store the index of this value into prev map (meaning visted)
        return
    

    @staticmethod
    def my_solution(nums: List[int], target: int) -> List[int]:

        results = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)-i):
                if nums[i] + nums[i+j] == target:
                    results.extend([i, i+j])
        return results

