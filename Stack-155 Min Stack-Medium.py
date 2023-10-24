'''155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.


Example 1:

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

Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.

'''
class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self,val):
        self.stack.append(val)
        val=min(val,self.minstack[-1] if self.minstack else val) #if selfstack not empty give minstacks last value if empty put val in minstack
        self.minstack.append(val)
        print("PUSH:stack:",self.stack)
        print("Minstack:",self.minstack)
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        print("POP:stack:", self.stack)
        print("Minstack:", self.minstack)

    def top(self):
        print("TOP :stack:", self.stack)
        print("Minstack:", self.minstack)
        return self.stack[-1]

    def getMin(self):
        print("GETMIN: stack:", self.stack)
        print("Minstack:", self.minstack)
        return self.minstack[-1]

commands=["MinStack","push","push","push","getMin","pop","top","getMin"]
values=[[],[-2],[0],[-3],[],[],[],[]]

min_stack=MinStack()

output = []

for cmd,val in zip(commands,values):
    if cmd=="push":
        min_stack.push(val)
    elif cmd=="pop":
        min_stack.pop()
    elif cmd=="top":
        output.append(min_stack.top())
    elif cmd=="getMin":
        output.append(min_stack.getMin())

print("\nOutput is:",output)

