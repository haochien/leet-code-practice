from utils.util_tree import BinaryTreeNode
from typing import List

class SortedArrayToBST:
    """
    LeetCode Question Nr.108
    https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

    Given an integer array nums where the elements are sorted in ascending order, convert it to a  height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

    Example 1:

            0
          /   \
        -3      9
       /       /   
    -10       5    

    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

            0
          /    \
        -10      5
         \        \
          -3        9

    Example 2:

        3     1
      /         \
    1             3       

    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
    """

    @staticmethod
    def great_ans1(nums: List[int]) ->  BinaryTreeNode:
        """
        technique: Recursive
        Time: O(n)
        Memory: O(n)

        https://www.youtube.com/watch?v=0K0uCMYq5ng
        """

        def helper(left, right):
            if left > right:
                return

            mid = (left + right) // 2
            root = BinaryTreeNode(nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
            
        
        final_tree = helper(0, len(nums) - 1)
        return final_tree

