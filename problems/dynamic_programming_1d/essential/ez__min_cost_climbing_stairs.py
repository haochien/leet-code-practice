from typing import List

class MinCostClimbingStairs:
    """
    LeetCode Question Nr.746
    https://leetcode.com/problems/min-cost-climbing-stairs/description/

    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
    Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.
    Return the minimum cost to reach the top of the floor.

    Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
    - Pay 15 and climb two steps to reach the top.
    The total cost is 15.

    Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: You will start at index 0.
    - Pay 1 and climb two steps to reach index 2.
    - Pay 1 and climb two steps to reach index 4.
    - Pay 1 and climb two steps to reach index 6.
    - Pay 1 and climb one step to reach index 7.
    - Pay 1 and climb two steps to reach index 9.
    - Pay 1 and climb one step to reach the top.
    The total cost is 6.
    """

    @staticmethod
    def great_ans1(cost: List[int]) -> int:
        """
        technique: Top-Down DP (dynamic programming)
        Time: O(n) 
        Memory: O(n)
        Expination Sources:
        https://www.youtube.com/watch?time_continue=1139&v=ktmzAZWkEZ0&embeds_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=Mjg2NjYsMjM4NTE&feature=emb_title

        my note: 
        from following chart, we can know, we can calcualte the cost for node(0), node(1), and node(2) just once, (caching)
        because the same know has the same result no matter where the node position is.
        so cost of 
        min cost node(2): 20
        min cost node(1): min(20+15, 15) = 15
        min cost node(0): min(10+15, 10+20) = 25
        ans: min(15, 20)  

                                       0
							   (10) /      \ (10)
								  1          2
					       (15) /    \(15)  / (20)  
			                  2        3    3
					   (20) / 
				          3
        
        Simplify:
        init cost for step [0,1,2,3]: [10 ,15 ,20 ,0]  
        cost calculation: (calculate backward (from final index)): [min(10+15, 10+20)=25 ,min(15+20, 15+0)=15 ,min(20+0, 20+0)=20 ,0]  
        """

        cost.append(0) # add initial cost of the top(destination) stair

        for i in range(len(cost)-3, -1, -1):  # -3 because this is the first stair has two step to go
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        
        return min(cost[0], cost[1])

   