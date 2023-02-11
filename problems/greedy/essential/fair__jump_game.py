from typing import List

class JumpGame:
    """
    LeetCode Question Nr.55
    https://leetcode.com/problems/jump-game/
    
    You are given an integer array nums. You are initially positioned at the array's first index, 
    and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. 
    Its maximum jump length is 0, which makes it impossible to reach the last index.

    """

    @staticmethod
    def great_ans1(nums: List[int]) -> List[List[int]]:
        """
        technique: greedy
        Time: O(n)
        Memory: O(1)
        https://youtu.be/Yan0cv2cLy8
        """

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal==0 else False



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


        
