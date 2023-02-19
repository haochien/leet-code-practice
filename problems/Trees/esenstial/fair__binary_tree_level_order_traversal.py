from utils.util_tree import BinaryTreeNode
from typing import List

class BTLevelOrderTraversal:
    """
    LeetCode Question Nr.102
    https://leetcode.com/problems/binary-tree-level-order-traversal/description/
    
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]

    Example 3:
    Input: root = []
    Output: []
    """


    @staticmethod
    def my_solution(root: BinaryTreeNode) -> List[List[int]]:
        """
        technique: BFS
        Time: O(n)
        Memory: O(n)
        """

        if root:
            layer_nodes = [root]
        else:
            return []

        res = [[root.val]]
        while layer_nodes:
            stack = []
            tmp = []

            for node in layer_nodes:
                if node.left:
                    stack.append(node.left)
                    tmp.append(node.left.val)

                if node.right:
                    stack.append(node.right)
                    tmp.append(node.right.val)

            if len(tmp) > 0:
                res.append(tmp)

            layer_nodes = stack

        return res
