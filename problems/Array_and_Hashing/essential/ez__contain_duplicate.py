from typing import List

class ContainsDuplicate:
    """
    LeetCode Question Nr.217
    https://leetcode.com/problems/contains-duplicate/

    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

    Input: nums = [1,2,3,1]  Output: true
    Input: nums = [1,1,1,3,3,4,3,2,4,2]  Output: true
    Input: nums = [1,2,3,4]  Output: false


    Good Analysis answer: 
    https://leetcode.com/problems/contains-duplicate/discuss/1698064/5-Different-Approaches-w-Explanations
    """

    @staticmethod
    def great_ans1(nums: List[int]) -> bool:
        """
        technique: Hash Map
        Time: O(n) : looping cause O(n) and Hashmap contribute O(1) (average : O(1)  ; worst case (collision) O(n/k))
        Memory: O(n)
        https://www.youtube.com/watch?v=3OamzN90kPg
        """

        # since we only record the value (no need to record index or other info), using hash set would be properer than hash table
        # And don't use list, appending list can cause pretty bad performance issue when the input list is huge (see my_solution1)
        hashset = set()
        # hashtable = {}

        for i in nums:
            if i in hashset:
                return True

            hashset.add(i)
            # hashtable[i] = 1

        return False


    @staticmethod
    def my_solution1(nums: List[int]) -> bool:

        """
        This is OVERTIME solution:
        list append has amortized O(1) complexity for huge list (O(n) - O(n^2))
        https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1
        """

        stack = []
        for i in nums:
            if i in stack:
                return True
            stack.append(i)
        return False
    

    @staticmethod
    def my_solution2(nums: List[int]) -> bool:
        """
        technique: Sort
        Time: O(nlogn) : looping cause O(n) and sorting (Timsort) contribute additional more
        Memory: O(1)
        """
        nums.sort()
        for index, i in enumerate(nums):
            if index == len(nums) -1:
                return False

            if i == nums[index+1]:
                return True
        
        return False
