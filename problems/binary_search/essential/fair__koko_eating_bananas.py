from typing import List
from math import ceil

class KokoEatBananas:
    """
    LeetCode Question Nr.875
    https://leetcode.com/problems/koko-eating-bananas/

    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
    If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    Return the minimum integer k such that she can eat all the bananas within h hours.


    Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4

    Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

    Example 3:
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23
    """
    @staticmethod
    def great_ans1(piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = (r - l) // 2 + l

            if sum([ceil(b / k) for b in piles]) <= h:
                r = k - 1
            else:
                l = k + 1

        return l



    @staticmethod
    def my_solution(piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        minK, maxK = 1, max(piles)
        res = maxK

        while minK <= maxK:
            midK = (minK + maxK) // 2
            times = 0
            for p in piles:
                times += p // midK + (p % midK > 0)
            
            if times <= h:
                res = min(midK, res)
                maxK = midK - 1
            else:
                minK = midK + 1
        return res
        
 
