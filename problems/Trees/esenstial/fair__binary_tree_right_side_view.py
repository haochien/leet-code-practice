from utils.util_tree import BinaryTreeNode
from typing import List

class BTRightSideView:
    """
    LeetCode Question Nr.199
    https://leetcode.com/problems/binary-tree-right-side-view/
    
    Given the root of a binary tree, imagine yourself standing on the right side of it, 
    return the values of the nodes you can see ordered from top to bottom.


    Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

    Example 2:
    Input: root = [1,null,3]
    Output: [1,3]

    Example 3:
    Input: root = []
    Output: []
    """


    @staticmethod
    def my_solution(root: BinaryTreeNode) ->  List[int]:
        if root:
            layer_nodes = [root]
        else:
            return []

        res = []
        while layer_nodes:
            stack = []

            if len(layer_nodes)>0 and layer_nodes[-1]:
                res.append(layer_nodes[-1].val)

            for node in layer_nodes:
                if node.left:
                    stack.append(node.left)
                    
                if node.right:
                    stack.append(node.right)
            
            layer_nodes = stack
        
        return res

