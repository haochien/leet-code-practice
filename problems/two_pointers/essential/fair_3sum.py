from typing import List

class SumThree:
    """
    LeetCode Question Nr.15
    https://leetcode.com/problems/3sum/

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.
    
    Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

    """

    @staticmethod
    def great_ans1(nums: List[int]) -> List[List[int]]:
        """
        technique: two pointers
        Time: O(n^2)
        Memory: O(n)
        https://www.youtube.com/watch?v=jzZsG8n2R9A
        """

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        


    @staticmethod
    def my_solution(nums: List[int]) -> List[List[int]]:
        """
        timeout
        """
        
        res = []
        res_check = []
        l, r = 0, 1

        while l < len(nums) - 2:
            while r < len(nums) - 1:
                target = -nums[l] + -nums[r]
                if ({nums[l], nums[r], target} not in res_check) and (target in nums[r+1:]):
                    res_check.append({nums[l], nums[r], target})
                    res.append([nums[l], nums[r], target])
                r += 1

            l += 1
            r = l + 1
        return res


    @staticmethod
    def my_solution2(nums: List[int]) -> List[List[int]]:
        """
        technique: two pointers
        Time: O(n^2)
        Memory: O(n)
        """

        res = []
        nums = sorted(nums)
        
        
        prev = None
        for i in range(len(nums)-1):
            if nums[i] == prev:
                continue
            
            l, r = i+1, len(nums) - 1
            prev_l_val, prev_r_val = None, None
            while l < r:
                if (nums[l] + nums[r] == -nums[i]) and (nums[l] != prev_l_val) and (nums[r] != prev_r_val):
                     res.append([nums[l], nums[r], nums[i]])
                     prev_l_val = nums[l]
                     prev_r_val = nums[r]
                     r -= 1
                     l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1
            
            prev = nums[i]

        
        return res
