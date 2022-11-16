from typing import List

class SingleNumber:
    """
    LeetCode Question Nr.704
    https://leetcode.com/problems/single-number/

    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Input: nums = [4,1,2,1,2]    Output: 4
    Input: nums = [2,2,1]    Output: 1
    Input: nums = [1]    Output: 1
    """

    @staticmethod
    def great_ans1(nums: List[int]) -> int:
        """
        tech use : bit manipulation / XOR
        https://leetcode.com/problems/single-number/discuss/1771771/Think-it-through-oror-Time%3A-O(n)-Space%3A-O(1)-oror-Python-Explained

        XOR:
        0^0 = 0 ; 1^1 = 0 ; 1^0 = 1
        2^2 = 0 ; 2^3 = 1 ; 
        2^0 = 2 ; 3^0 = 3 ;
        A^B^A = A^A^B : 1^2^3^2^3 = 1 ^ (2^2) ^ (3^3) = 1^0^0 = 1
        https://accu.org/journals/overload/20/109/lewin_1915/
        """
        
        res = 0
        for num in nums:
            res = res ^ num
        
        return res

    @staticmethod
    def my_solution1(nums: List[int]) -> int:
        """
        technique: hash mapping
        Time: O(n)
        Memory: O(n)
        """
        
        hash_set =set()
        for i in nums:
            hash_set.remove(i) if i in hash_set else hash_set.add(i)
                
        return list(hash_set)[0]


    @staticmethod
    def my_solution2(nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
                return nums[i]
            i += 1
        return nums[i]
            

