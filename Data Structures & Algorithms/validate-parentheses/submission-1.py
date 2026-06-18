class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []

        # Matching opening bracket for each closing bracket
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            # If opening bracket, push onto stack
            if char in "([{":
                stack.append(char)
            else:
                # Invalid if stack is empty
                if not stack:
                    return False

                # Check if top of stack matches current closing bracket
                if stack.pop() != pairs[char]:
                    return False

        # Valid only if all brackets were matched
        return len(stack) == 0


'''
Logic:
iterate through each character in the string
if the character is an opening bracket, push it onto the stack
if the character is a closing bracket:
check that the stack is not empty
check that the top of the stack is the matching opening bracket
if either check fails, return false
after processing all characters, return true only if the stack is empty

Pattern:
Stack (LIFO)

Time Complexity:
O(n)
we traverse the string once, and each bracket is pushed
and popped from the stack at most one time

Space Complexity:
O(n)
in the worst case, all characters are opening brackets
and are stored in the stack

Time to complete problem:
~12 minutes
'''