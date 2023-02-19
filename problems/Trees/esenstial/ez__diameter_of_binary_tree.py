from utils.util_tree import BinaryTreeNode

class DiameterOfBT:
    """
    LeetCode Question Nr.543
    https://leetcode.com/problems/diameter-of-binary-tree/
    
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.


    Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

    Example 2:
    Input: root = [1,2]
    Output: 1
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode) ->  int:
        """
        technique: DFS
        Time: O(n)
        Memory: O(1)
        https://youtu.be/bkxqA8Rfv04
        """
        max_lv = [0]
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            max_lv[0] = max(max_lv[0], left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return max_lv[0]
