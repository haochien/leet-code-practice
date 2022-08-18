class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CatagoryTreeNode:
    def __init__(self, data, parent=None, children=[]):
        self.data = data
        self.parent = parent
        self.children = children


class CatagoryTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def transfer_list_to_binary_treenode(lst):
    if len(lst) == 0:
        return None
    
    def _inner(index=0):
        if len(lst) <= index or lst[index] is None:
            return None
        
        node = BinaryTreeNode(lst[index])
        node.left = _inner(2 * index + 1)
        node.right = _inner(2 * index + 2)
        return node
    
    return _inner()


#root = transfer_list_to_binary_treenode([1,None,2,None,None,3,4])
