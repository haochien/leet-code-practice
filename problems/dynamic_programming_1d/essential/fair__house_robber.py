from typing import List

class HouseRobber:
    """
    LeetCode Question Nr.198
    https://leetcode.com/problems/house-robber/

    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
    it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.
    """

    @staticmethod
    def great_ans1(nums: List[int]) -> int:
        """
        technique: DP
        Time: O(n) 
        Memory: O(1)
        Expination Sources:
        https://youtu.be/73r3KWiEvyk
        """
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    @staticmethod
    def my_solution(nums: List[int]) -> int:
        """
        technique: Top-Down DP
        Time: O(n) 
        Memory: O(1)

        example:
        4, 7, 8, 6, 10, 20, 1

        max return for each node will be (backward calculating):
        [4+max(28,26,11,20,1)=32, 7+max(26,11,20,1)=33 ,8+max(11,20,1)=28 ,6+max(20,1)=26 ,10+1=11 ,20 ,1]

        when len(nums) <= 2, no adding should be considered. directly return the max.
        when len(nums) <= 2, backward looping starts from len(nums)-3.

        The trick here is that we need to reduce the time cost in max(...)
        And we can notice that first max starts from the final number i.e. len(nums)-1
        Then in each loop, we can always compare current index+1 with the max 
        The new max will then be added to the number of the next loop.
        """


        if len(nums) <= 2:
            return max(nums)

        max_index = len(nums)-1

        for i in range(len(nums)-3, -1, -1):
            nums[i] += nums[max_index]
            if nums[i+1] > nums[max_index]:
                max_index = i+1
        return max(nums[i], nums[max_index])


    @staticmethod
    def my_solution1(nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in nums[2:]:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2