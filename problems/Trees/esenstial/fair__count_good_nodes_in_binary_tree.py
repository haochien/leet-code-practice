from utils.util_tree import BinaryTreeNode

class CountGoodNodesInBT:
    """
    LeetCode Question Nr.1448
    https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
    
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

    Return the number of good nodes in the binary tree.


    Example 1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.

    Example 2:
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

    Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.
    """

    @staticmethod
    def great_ans1(root: BinaryTreeNode) ->  int:
        def dfs(node, max_parent_val):
            if not node:
                return 0

            res = 1 if node.val >= max_parent_val else 0
            
            res += dfs(node.left, max(node.val, max_parent_val))
            res += dfs(node.right, max(node.val, max_parent_val))
            return res


        return dfs(root, float('-inf'))


    @staticmethod
    def my_solution(root: BinaryTreeNode) ->  int:
        neg_inf = float('-inf')
        if root:
            layer_nodes = [(root, neg_inf)]  # (node, max_parent_val)
        else:
            return 0

        res = 0
        while layer_nodes:
            stack = []

            for node, max_parent_val in layer_nodes:
                if node.val >= max_parent_val:
                    res += 1

                if node.left:
                    stack.append((node.left, max(node.val, max_parent_val)))

                if node.right:
                    stack.append((node.right, max(node.val, max_parent_val)))

            layer_nodes = stack

        return res
