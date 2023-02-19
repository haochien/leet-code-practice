from utils.util_tree import BinaryTreeNode

class LowestCommonAncestorOfBST:
    """
    LeetCode Question Nr.235
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
    
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: 
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
    (where we allow a node to be a descendant of itself).”


    Example 1:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

    Example 2:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

    Example 3:
    Input: root = [2,1], p = 2, q = 1
    Output: 2
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode) ->  BinaryTreeNode:
        def dfs(root, p, q):
            if not root:
                return None

            node_min = min(p.val, q.val)
            node_max = max(p.val, q.val)
            
            if node_min <= root.val <= node_max:
                return root

            if node_max < root.val:
                return dfs(root.left, p, q)
            else:
                return dfs(root.right, p, q)

        return dfs(root, p, q)


    @staticmethod
    def my_solution(root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode) ->  BinaryTreeNode:
        node_min = min(p.val, q.val)
        node_max = max(p.val, q.val)

        while True:
            if node_min <= root.val <= node_max:
                return root
            
            if node_max < root.val:
                root = root.left
            else:
                root = root.right
