from utils.util_tree import BinaryTreeNode
from typing import List

class BinaryTreeInorderTraversal:
    """
    LeetCode Question Nr.101
    https://leetcode.com/problems/symmetric-tree/description/

    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    Example 1:
    1
      \
        2
      /
    3
    Input: root = [1,null,2,3]
    Output: [1,3,2]

    Example 2:
    Input: root = []
    Output: []

    Example 3:
    Input: root = [1]
    Output: [1]


    Note All DFS traversals (preorder, inorder, postorder):
    Traversal: [1,2,3,4,5]
                1
              /   \
            2       3
          /   \
        4       5
    DFS Preorder:
    Root -> Left -> Right: [1,2,4,5,3]
        
    DFS Inorder:
    Left -> Root -> Right: [4,2,5,1,3]

    DFS Postorder:
    Left -> Right -> Root: [4,5,2,3,1]

    Additional Info: 
    https://www.javatpoint.com/preorder-traversal
    https://www.javatpoint.com/inorder-traversal
    https://www.javatpoint.com/postorder-traversal
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode) ->  List[int]:
        """
        technique: Recursive
        Time: O(n)
        Memory: O(n)
        https://www.youtube.com/watch?v=g_S5WuasWUE
        """
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        inorder(root)
        return res



    @staticmethod
    def great_ans2(root: BinaryTreeNode) ->  List[int]:
        """
        technique: Iterative
        
        In inorder, the order should be
        left -> root -> right
        But when we use stack, the order should be reversed:
        right -> root -> left
        """

        def inorderTraversal(root: BinaryTreeNode) -> List[int]:
            res, stack = [], [(root, False)]
            while stack:
                node, visited = stack.pop()  # the last element
                if node:
                    if visited:
                        res.append(node.val)
                    else:  # inorder: left -> root -> right
                        stack.append((node.right, False))
                        stack.append((node, True))
                        stack.append((node.left, False))
            return res


        def preorderTraversal(root: BinaryTreeNode) -> List[int]:
            """
            In preorder, the order should be
            root -> left -> right
            But when we use stack, the order should be reversed:
            right -> left -> root
            """
            res, stack = [], [(root, False)]
            while stack:
                node, visited = stack.pop()  # the last element
                if node:
                    if visited:  
                        res.append(node.val)
                    else:  # preorder: root -> left -> right
                        stack.append((node.right, False))
                        stack.append((node.left, False))
                        stack.append((node, True))
            return res


        def postorderTraversal(root: BinaryTreeNode) -> List[int]:
            """
            In postorder, the order should be
            left -> right -> root
            But when we use stack, the order should be reversed:
            root -> right -> left
            """
            res, stack = [], [(root, False)]
            while stack:
                node, visited = stack.pop()  # the last element
                if node:
                    if visited:
                        res.append(node.val)
                    else:  # postorder: left -> right -> root
                        stack.append((node, True))
                        stack.append((node.right, False))
                        stack.append((node.left, False))
            return res
        

        return inorderTraversal(root)