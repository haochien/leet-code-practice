from utils.util_tree import BinaryTreeNode

class SameTree:
    """
    LeetCode Question Nr.100
    https://leetcode.com/problems/same-tree/

    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Input: p = [1,2,3], q = [1,2,3]    Output: true
    Input: p = [1,2], q = [1,null,2]    Output: false
    Input: p = [1,2,1], q = [1,1,2]    Output: false
    """

    @staticmethod
    def my_solution(p: BinaryTreeNode, q: BinaryTreeNode) -> bool:
        """
        technique: Depth First Search (DFS)
        https://www.techiedelight.com/depth-first-search/

        Time: O(n)
        Memory: O(1)
        
        great reference:
        https://youtu.be/vRbbcKXCxOw
        """

        def _is_same_tree(p, q):
            if not p and not q: 
                # if both p and q are None (empty tree)
                return True
            
            if not p or not q or p.val != q.val:
                # if only one of p or q is empty or the value for both are different
                return False
        
            return (_is_same_tree(p.left, q.left) and 
                    _is_same_tree(p.right, q.right))
        
        return (_is_same_tree(p, q))