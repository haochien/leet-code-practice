from utils.util_tree import BinaryTreeNode
from typing import List

class SymmetricTree:
    """
    LeetCode Question Nr.94
    https://leetcode.com/problems/binary-tree-inorder-traversal/

    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    
    Example 1:
            1
         /     \
        2        2
      /   \    /   \
     3     4  4     3
    Input: root = [1,2,2,3,4,4,3]
    Output: true

    Example 2:
            1
         /     \
        2        2
         \        \
          3        3
    Input: root = [1,2,2,null,3,null,3]
    Output: false
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode) ->  List[int]:
        """
        technique: Recursive
        Time: O(n)
        Memory: O(logn)
        """
        def is_symmetric(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False 

            if left.val == right.val:
                out_pair = is_symmetric(left.left, right.right)
                in_pair = is_symmetric(left.right, right.left)
                return out_pair and in_pair
            else:
                return False
        
        if not root:
            return True

        return  is_symmetric(root.left, root.right)




    @staticmethod
    def great_ans2(root: BinaryTreeNode) ->  List[int]:
        """
        technique: Iterative

        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue

            if not left or not right or (left.val != right.val):
                return False
            
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True