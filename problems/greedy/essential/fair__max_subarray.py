from typing import List

class MaxSubarray:
    """
    LeetCode Question Nr.53
    https://leetcode.com/problems/maximum-subarray/
    
    Given an integer array nums, find the subarray with the largest sum, and return its sum.

    Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

    Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
    """

    @staticmethod
    def great_ans1(nums: List[int]) -> List[List[int]]:
        """
        technique: greedy
        Time: O(n)
        Memory: O(1)
        https://www.youtube.com/watch?v=5WZl3MMT0Eg&t=3s

        """

        max_res = nums[0]
        temp_sum = 0

        for i in nums:
            if temp_sum < 0:
                temp_sum = 0

            temp_sum += i
            max_res = max(max_res, temp_sum)
        
        return max_res



    @staticmethod
    def great_ans2(nums: List[int]) -> int:
        """
        technique: dp
        Time: O(n)
        Memory: O(1)
        https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/?orderBy=most_votes
        """
        # #Brute-Force
        # def maxSubArray(nums):
        #     ans = -10000000000000000
        #     for i in range(len(nums)):
        #         cur_sum = 0
        #         for j in range(i, len(nums)):
        #             cur_sum += nums[j]
        #             ans = max(ans, cur_sum)
        #     return ans



        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + nums[i-1]) 

        return max(dp)
        
