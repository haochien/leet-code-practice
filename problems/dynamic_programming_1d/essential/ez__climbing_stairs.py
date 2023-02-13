import math

class ClimbingStairs:
    """
    LeetCode Question Nr.70
    https://leetcode.com/problems/climbing-stairs/

    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Input: n = 2  Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Input: n = 3  Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """

    @staticmethod
    def great_ans1(n: int) -> int:
        """
        technique: Top-Down DP (dynamic programming)
        Time: O(n) 
        Memory: O(n)
        Expination Sources:
        https://leetcode.com/problems/climbing-stairs/solutions/1792723/python-in-depth-walkthrough-explanation-dp-top-down-bottom-up/

        my note: 
        The ways of n is actually determined by ways of n-1 and ways of n-2
        The trick here is that the number of ways for n can have been calcuated in previous around.
        For example: in following tree, cS(4) has been calcuated twice, and cS(2) has been calculated by 5 times.
        So once the number of ways for n has been calcuated, we can store it in memory and fetch it directly in next time
        

                                       climbStairs(6)
									 /               \
								cS(5)       +          cS(4)
					           /    \                  /    \
			               cS(4)   +   cS(3)         cS(3) + cS(2)
						   /  \        /   \         /   \
				      cS(3) + cS(2) cS(2) + cS(1) cS(2) + cS(1)
					  /  \
			     cS(2) + cS(1)
        """

        def __climb_naive_recursion(n):
            """
            This will need time O(2^n) and will cause time out, so need the support from memory
            to prevent the calucated n being calcuated again
            """
            if n <= 2:
                return n
            else:
                return __climb_naive_recursion(n - 1) + __climb_naive_recursion(n - 2)
        
        def __climb_with_cache(n):
            if n in solution_cache:
                return solution_cache[n]
            
            solution_cache[n] = __climb_with_cache(n - 1) + __climb_with_cache(n - 2)
            return solution_cache[n]
        
        solution_cache = {1: 1, 2: 2}  # base case: n=1 has only 1 way ; n=2 has two ways
        return __climb_with_cache(n)
    

    @staticmethod
    def great_ans2(n: int) -> int:
        """
        technique: Bottom-Up DP
        Time: O(n) 
        Memory: O(n)
        Expination Sources:
        https://leetcode.com/problems/climbing-stairs/solutions/1792723/python-in-depth-walkthrough-explanation-dp-top-down-bottom-up/
        https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=45s

        my note: 
        we saw that the number of ways to climb n stairs depends on the number of ways to climb n - 1 and n - 2 stairs. 
        So instead of going top-down and computing these values recursively, we compute them bottom-up, 
        starting with the base cases and building upon the previous values until we reach n. We use a dp array of length n + 1
        """
        if n <=2:
            return n
        
        res = [-1] * n
        res[0], res[1] = 1, 2  # base case: n=1 has only 1 way ; n=2 has two ways

        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]

        return res[-1]



    @staticmethod
    def my_solution(n: int) -> int:
        
        def __factorial(n):
            # if math.factorial is not allowed
            fact = 1
            for num in range(2, n + 1):
                fact *= num
            return fact

        x = 0
        y = 0
        result_count = 0

        while n >= 1*x:
            if 1*x + 2*y == 0:
                result_count += math.factorial(x+y) / (math.factorial(x) * math.factorial(y))
                x += 1 
                y = 0
            elif 1*x + 2*y > 0:
                x += 1 
                y = 0
            else:
                y += 1
        return result_count



