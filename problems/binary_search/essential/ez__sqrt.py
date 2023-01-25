
class Sqrt:
    """
    LeetCode Question Nr.69
    https://leetcode.com/problems/sqrtx/

    Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
    You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

    Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

    Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

    """

    @staticmethod
    def great_ans1(x: int) -> int:
        """
        technique: binary search
        Time: O(logn) 
        Memory: O(1)
        """
        l, r = 0, x
        while l <= r:
            mid = (l+r) // 2
            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
            else:
                return mid
        
        # When there is no perfect square, r is the the value on the left
        # of where it would have been (rounding down). If we were rounding up, 
        # we would return l
        return r




