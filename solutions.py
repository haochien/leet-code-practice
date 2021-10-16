from typing import List


class Solution:
    def twoSum_my(self, nums: List[int], target: int) -> List[int]:
        """
        Leet Code Question Nr.1
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Input: nums = [2,7,11,15], target = 9  Output: [0,1]
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


    def palindrome_number_my(self, x: int) -> bool:
        """
        Leet Code Question Nr.9
        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

        Input: x = 121  Output: true
        """
        x = str(x)
        right_index = len(x) - 1
        left_index = 0
        while left_index < right_index:
            if x[left_index] == x[right_index]:
                left_index += 1
                right_index -= 1
            else:
                return False
        return True


    def palindrome_number_ans1(self, x: int) -> bool:
        """
        int is allowed to converted to str
        https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


    def palindrome_number_ans2(self, x: int) -> bool:
        """
        int is not allowed to converted to str
        """
        if x < 0:
            return False

        input_nb = x
        recreate_nb = 0
        while x > 0:
            recreate_nb = recreate_nb * 10 + x%10
            x = x//10
        return recreate_nb == input_nb


    def palindrome_number_ans3(self, x: int) -> bool:
        """
        int is not allowed to converted to str & Advanced and faster solution
        """
        if x < 0 or (x > 0 and x%10 == 0):
            return False

        recreate_nb = 0
        while x > recreate_nb:
            recreate_nb = recreate_nb * 10 + x%10
            x = x//10
        return True if recreate_nb == x or recreate_nb//10 == x else False