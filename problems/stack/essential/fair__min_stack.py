
class MinStack:
    """
    LeetCode Question Nr.155
    https://leetcode.com/problems/min-stack/
    
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    """

    class MySolution:
        def __init__(self):
            self.stack = []
            self.min = []


        def push(self, val: int) -> None:
            self.stack += [val]
            if len(self.min)==0 or val < self.min[-1]:
                self.min += [val]
            else:
                self.min += [self.min[-1]]
            return
            
        def pop(self) -> None:
            if len(self.stack) > 0:
                self.stack = self.stack[:-1]
            
            if len(self.min) > 0:
                self.min = self.min[:-1]

            return

        def top(self) -> int:
            return self.stack[-1] if len(self.stack) > 0 else []
            

        def getMin(self) -> int:
            return self.min[-1] if len(self.min) > 0 else []
        

        def execute(self):
            self.push(-2)
            self.push(0)
            self.push(-3)
            self.getMin()
            self.pop()
            self.top()
            self.getMin()
            return self.stack


