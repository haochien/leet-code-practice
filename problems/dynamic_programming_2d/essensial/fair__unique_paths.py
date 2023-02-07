
class UniquePaths:
    """
    LeetCode Question Nr.62
    https://leetcode.com/problems/unique-paths/

    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
    The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 109.

    Example 1:
    Input: m = 3, n = 7
    Output: 28

    Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

    """

    @staticmethod
    def great_ans1(m: int, n: int) -> int:
        """
        technique: DP
        Time: O(n) 
        Memory: O(n)
        Expination Sources:
        https://youtu.be/IlEsdxuD4lY

        Expination:
        take m = 3, n = 7 as example:
        1. button row solusion : [1, 1, 1, 1, 1, 1, 1] only go right 1 way
        2. second row solusion : [1+6=7, 1+5=6, 1+4=5, 1+3=4, 1+2=3, 1+1=2, 1]  the current cell solusion always equal to its right and below cells
        2. top row solusion :    [7+21=28, 6+15=21, 5+10=15, 4+6=10, 3+3=6, 1+2=3, 1]  same calculation like second row

        """

        bottom_row = [1] * n
        m -= 1

        while m > 0:
            new_row = [1] * n
            for i in range(n-2, -1, -1):
                new_row[i] = new_row[i+1] + bottom_row[i]
            
            bottom_row = new_row
            m -=1
        
        return bottom_row[0]


