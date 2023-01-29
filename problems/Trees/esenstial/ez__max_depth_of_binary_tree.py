from utils.util_tree import BinaryTreeNode
from typing import List

class MaxDepthBinaryTree:
    """
    LeetCode Question Nr.101
    https://leetcode.com/problems/symmetric-tree/description/

    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Example 1:
            3
          /   \
        9       20
               /   \
             15     7

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Example 2:
    Input: root = [1,null,2]
    Output: 2
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode) ->  List[int]:
        """
        technique: Recursive
        Time: O(n)
        Memory: O(n)
        """

        def df_search(root, depth):
            if not root:
                return depth

            left_depth = df_search(root.left, depth+1)
            right_depth = df_search(root.right, depth+1)

            return max(left_depth, right_depth)
            
        
        return df_search(root, 0)


    @staticmethod
    def great_ans2(root: BinaryTreeNode) ->  List[int]:
        """
        technique: Iterative

        """

        depth = 0
        layer = [root] if root else []

        while layer:
            depth += 1
            stack = []

            for node in layer:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            layer = stack
        return depth