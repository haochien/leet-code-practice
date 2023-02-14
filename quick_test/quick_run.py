
def test_run(s):

    stack = []
    dict_map = {"]":"[", "}":"{", ")":"("}
    
    for i in s:
        if i not in dict_map:
            stack.append(i)
        else:
            if len(stack) == 0 or dict_map[i] != stack.pop():
                return False

    return True if len(stack) == 0 else False


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
    result = test_run("([)]")
    result = TestRun().execute()
    print(f"result: {result}")