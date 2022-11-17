class ValidPalindrome:
    """
    LeetCode Question Nr.217
    https://leetcode.com/problems/valid-palindrome/

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
    removing all non-alphanumeric characters, it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.


    Input: s = "A man, a plan, a canal: Panama"  Output: true  Explanation: "amanaplanacanalpanama" is a palindrome.
    Input: s = " "  Output: true
    Input: s = "race a car"  Output: false
    """

    @staticmethod
    def great_ans1(s: str) -> bool:
        """
        technique: two pointers
        Time: O(n)
        Memory: O(n)
        https://www.youtube.com/watch?v=jJXJ16kPFWg
        """

        def _alphaNum(char):
            # ord check the ASCII index of the character
            return (ord('A') <= ord(char) <= ord('Z') or 
                    ord('a') <= ord(char) <= ord('z') or 
                    ord('0') <= ord(char) <= ord('9'))

        lst_s = [char.lower() for char in s if _alphaNum(char)]
        l, r = 0, len(lst_s)-1
        while l < r:
            if lst_s[l] != lst_s[r]:
                return False
            l += 1
            r -= 1

        # if don't tackle alphanumeric in beginning:
        # while l < r:
        #     while l < r and not _alphaNum(s[l]): l += 1
        #     while l < r and not _alphaNum(s[r]): r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        
        return True
    

    @staticmethod
    def great_ans2(s: str) -> bool:
        lst_s = [char.lower() for char in s if char.isalnum()] 
        return lst_s == lst_s[::-1]
    

    @staticmethod
    def my_solution(s: str) -> bool:
        alpha_numeric = [char for char in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        s = s.lower()
        lst_s = [char for char in s if char in alpha_numeric]

        i = 0
        while len(lst_s) > 1 and i < len(lst_s)-1:
            if lst_s[i] != lst_s.pop():
                return False
            i += 1

        return True
