
class LongestSubstringWithoutRepeat:
    """
    LeetCode Question Nr.3
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    
    Given a string s, find the length of the longest substring without repeating characters.
    A substring is a contiguous non-empty sequence of characters within a string.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    @staticmethod
    def great_ans1(s: str) -> int:
        """
        technique: sliding window
        Time: O(n)
        Memory: O(n)
        https://www.youtube.com/watch?v=wiGpQwVHdE0
        """
        
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res
            


    @staticmethod
    def my_solution(s: str) -> int:
        """
        Time: O(n)
        Memory: O(n)
        """

        if len(s) < 2:
            return len(s)
        
        l, r = 0, 1
        checked = set(s[l])
        longest_length = 1

        while r < len(s) and l <= r:
            if s[r] not in checked:
                checked.add(s[r])
                longest_length = len(checked) if len(checked) > longest_length else longest_length
                r += 1
            else:
                checked.remove(s[l])
                l += 1


        
        return longest_length

    