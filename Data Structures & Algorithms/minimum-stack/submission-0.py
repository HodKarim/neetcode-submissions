class MinStack:

    def __init__(self):
        # Store all values
        self.stack = []

        # Store minimum value at each position
        self.minStack = []

    def push(self, val: int) -> None:
        # Add value to main stack
        self.stack.append(val)

        # First element becomes the minimum
        if not self.minStack:
            self.minStack.append(val)
        else:
            # Store the current minimum
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        # Remove from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return top value
        return self.stack[-1]

    def getMin(self) -> int:
        # Return current minimum
        return self.minStack[-1]


'''
Logic:
use two stacks:
one stack stores all values normally
the second stack stores the minimum value seen so far at each position

when pushing:
add the value to the main stack
add the smaller of:
the current value
the current minimum
to the min stack

when popping:
remove the top element from both stacks

top returns the last value in the main stack

getMin returns the last value in the min stack,
which is always the minimum element currently in the stack

Pattern:
Stack + Auxiliary Stack

Time Complexity:
push: O(1)
pop: O(1)
top: O(1)
getMin: O(1)

Space Complexity:
O(n)
we store up to n elements in both stacks

Time to complete problem:
~27 minutes
'''