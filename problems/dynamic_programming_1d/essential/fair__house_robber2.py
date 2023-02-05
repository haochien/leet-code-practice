from typing import List

class HouseRobber2:
    """
    LeetCode Question Nr.213
    https://leetcode.com/problems/house-robber-ii/

    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
    All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
    Meanwhile, adjacent houses have a security system connected, 
    and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.

    Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

    Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    """

    @staticmethod
    def great_ans1(nums: List[int]) -> int:
        """
        technique: DP
        Time: O(n) 
        Memory: O(1)
        Expination Sources:
        https://www.youtube.com/watch?v=rWAJCfYYOvM
        """

        def helper(nums):
            rob1, rob2 = nums[0], max(nums[0], nums[1])
            for i in nums[2:]:
                temp = max(rob1 + i, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        

        if len(nums) <= 2:
            return max(nums)
        
        return max(helper(nums[:-1]), helper(nums[1:]))
        
        # def helper(nums):
        #     rob1, rob2 = 0, 0
        #     for i in nums:
        #         temp = max(rob1 + i, rob2)
        #         rob1 = rob2
        #         rob2 = temp

        #     return rob2
   
        # return max(nums[0], helper(nums[:-1]), helper(nums[1:]))
             



    @staticmethod
    def my_solution(nums: List[int]) -> int:
        """
        technique: DP
        Time: O(n^2) 
        Memory: O(1)
        """


        if len(nums) <= 2:
            return max(nums)

        max_rob = 0
        for arr_index in range(0, len(nums)):
            new_nums = nums[arr_index:] + nums[0:arr_index]
            new_nums.pop()

            rob1, rob2 = new_nums[0], new_nums[1]
            for i in new_nums[2:]:
                temp = max(rob1 + i, rob2)
                rob1 = rob2
                rob2 = temp

            max_rob = rob2 if rob2 > max_rob else max_rob
        
        return max_rob

   