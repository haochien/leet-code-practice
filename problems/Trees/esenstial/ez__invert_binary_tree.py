from utils.util_tree import BinaryTreeNode
import collections

class InvertBinaryTree:
    """
    LeetCode Question Nr.226
    https://leetcode.com/problems/invert-binary-tree/

    Given the root of a binary tree, invert the tree, and return its root.


    Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

    Example 3:
    Input: root = []
    Output: []
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode) ->  BinaryTreeNode:
        """
        technique: DFS stack
        Time: O(n)
        Memory: O(n)
        https://leetcode.com/problems/invert-binary-tree/solutions/62705/python-solutions-recursively-dfs-bfs/
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root


    @staticmethod
    def great_ans2(root: BinaryTreeNode) ->  BinaryTreeNode:
        """
        technique: BFS stack
        Time: O(n)
        Memory: O(n)
        https://leetcode.com/problems/invert-binary-tree/solutions/62705/python-solutions-recursively-dfs-bfs/
        """
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root


    @staticmethod
    def my_solution(root: BinaryTreeNode) ->  BinaryTreeNode:
        """
        technique: DFS recursively
        Time: O(n)
        Memory: O(1)
        https://youtu.be/OnSn2XEQ4MY
        """
        
        def dfs(node):
            if not node:
                return None
            
            temp = node.left
            node.left = node.right
            node.right = temp

            dfs(node.left)
            dfs(node.right)
            return node
 
        return dfs(root)