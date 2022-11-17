class PalindromeNumber:
    """
    LeetCode Question Nr.9
    https://leetcode.com/problems/palindrome-number/

    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

    Input: x = 121  Output: true
    Input: x = -121  Output: false
    Input: x = 10  Output: false
    """

    @staticmethod
    def my_solution(x: int) -> bool:
        """
        technique: two pointers
        Time: O(n)
        Memory: O(n)
        """

        x = str(x)
        r = len(x) - 1
        l = 0
        while l < r:
            if x[l] != x[r]:
                return False    
            l += 1
            r -= 1

        return True

    @staticmethod
    def great_ans1(x: int) -> bool:
        """
        int is allowed to converted to str
        https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


    @staticmethod
    def great_ans2(x: int) -> bool:
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


    @staticmethod
    def great_ans3(x: int) -> bool:
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