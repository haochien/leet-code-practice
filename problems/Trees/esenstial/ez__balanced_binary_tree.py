from utils.util_tree import BinaryTreeNode

class BalancedBT:
    """
    LeetCode Question Nr.110
    https://leetcode.com/problems/balanced-binary-tree/
    
    Given a binary tree, determine if it is height-balanced.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

    Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode) ->  bool:
        """
        https://www.youtube.com/watch?v=QfJsau0ItOY
        """
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


    @staticmethod
    def my_solution(root: BinaryTreeNode) ->  bool:
        res = [True]

        def dfs(root):
            if not root:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            if abs(left_depth - right_depth) > 1:
                res[0] = False
            
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return res[0]
