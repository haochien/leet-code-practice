from typing import List

class JumpGame2:
    """
    LeetCode Question Nr.45
    https://leetcode.com/problems/jump-game-ii/
    
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and i + j < n
    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. 
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2
    """

    @staticmethod
    def great_ans1(nums: List[int]) -> List[List[int]]:
        """
        technique: greedy
        Time: O(n)
        Memory: O(1)
        https://www.youtube.com/watch?v=dJ7sWiOoK7g
        """

        l, r = 0, 0
        count = 0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            count += 1
        
        return count

        



    @staticmethod
    def my_solution(nums: List[int]) -> bool:
        """
        technique: greedy
        Time: O(n)
        Memory: O(1)

        note:
        starting from last second index, and you need at least 1 step to reach final index.
        If the last second index does not match this requirement, you would then check the last third index and this time requires 2 steps.
        If it match require step, then required_step will be set back to 1
        """

        if len(nums) == 1:
            return True

        required_step = 1
        for i in range (len(nums)-2, -1, -1):
            if nums[i] < required_step:
                required_step += 1
                can_finish = False
            else:
                can_finish = True
                required_step = 1

        return can_finish


        
