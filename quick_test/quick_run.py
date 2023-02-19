class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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



def test_run(root):

    layer_nodes = [root]

    while layer_nodes:
        stack = []

        for node in layer_nodes:
            if node.left is None and node.right is None:
                continue

            if node.left is None or node.right is None:
                return False

            if not (node.left.val < node.val < node.right.val):
                return False

            if node.left is not None:
                stack.append(node.left)
            
            if node.right is not None:
                stack.append(node.right)
            
        layer_nodes = stack
    return True



class TestRun:
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, val):
        self.stack += [val]
        if len(self.min) == 0 or self.min[-1] >= val:
            self.min += [val]
        else:
            self.min += [self.min[-1]]
    
    def pop(self):
        if len(self.stack) > 0:
            self.stack = self.stack[:-1]
            self.min = self.min[:-1]
    
    def top(self):
        return self.stack[-1] if len(self.stack) > 0 else []
    
    def getMin(self):
        return self.min[-1] if len(self.stack) > 0 else []

    def execute(self):
        self.push(-2)
        self.push(0)
        self.push(-3)
        self.getMin()
        self.pop()
        self.top()
        self.getMin()
        return self.stack



if __name__ == '__main__':
    result = test_run(transfer_list_to_binary_treenode([2,1,3]))
    # result = TestRun().execute()
    print(f"result: {result}")