from typing import List

class NumberOfOneBits:
    """
    LeetCode Question Nr.191
    https://leetcode.com/problems/number-of-1-bits/

    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

    Note:
    Note that in some languages, such as Java, there is no unsigned integer type. In this case, 
    the input will be given as a signed integer type. It should not affect your implementation, 
    as the integer's internal binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. 
    Therefore, in Example 3, the input represents the signed integer. -3.

    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
    """

    @staticmethod
    def great_ans1(n: int) -> int:
        """
        tech use : bit manipulation 
        Time: O(1) (actually O(32) since input is 32 bit)
        Memory: O(1)

        https://www.youtube.com/watch?v=5Km3utixwZs

        idea for solve 1011:
        init  : 101"1" % 2 => get 1
        shift : 10"1" % 2 => get 1
        shift : 1"0" % 2 => get 0
        shift : "1" % 2 => get 1
        shift : only 0 left, then return
        """
        
        res = 0
        while n > 0:
            res += n % 2
            n = n >> 1
        return res



            

