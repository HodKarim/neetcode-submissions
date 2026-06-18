class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # If token is an operator, perform the operation
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    # Division truncates toward zero
                    stack.append(int(a / b))

            else:
                # Push numbers onto the stack
                stack.append(int(token))

        return stack[-1]


'''
Logic:
iterate through each token in the expression

if the token is a number:
push it onto the stack

if the token is an operator:
pop the top two numbers from the stack
perform the operation
push the result back onto the stack

continue until all tokens are processed

the final value remaining in the stack is the answer

Pattern:
Stack

Time Complexity:
O(n)
we process each token exactly once

Space Complexity:
O(n)
in the worst case, all tokens are numbers and stored in the stack

Time to complete problem:
~38 minutes
'''