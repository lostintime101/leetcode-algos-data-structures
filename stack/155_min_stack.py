import unittest

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    
You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class TestMinStack(unittest.TestCase):

    def test_push_pop(self):
        stack = MinStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(len(stack.stack), 0)

    def test_top(self):
        stack = MinStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        self.assertEqual(stack.top(), 2)
        stack.pop()
        self.assertEqual(stack.top(), 1)

    def test_getMin(self):
        stack = MinStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        self.assertEqual(stack.getMin(), 1)
        stack.pop()
        self.assertEqual(stack.getMin(), 1)
        stack.pop()
        self.assertRaises(IndexError, stack.getMin)


if __name__ == '__main__':
    unittest.main()
