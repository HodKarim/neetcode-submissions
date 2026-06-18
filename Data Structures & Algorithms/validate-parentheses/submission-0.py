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


# Logic:
# 1. Use a stack to keep track of opening brackets.
# 2. Push opening brackets onto the stack.
# 3. When a closing bracket is found:
#    - Stack must not be empty.
#    - Top of the stack must be the matching opening bracket.
# 4. If any mismatch occurs, return False.
# 5. At the end, the stack must be empty for the string to be valid.

# Pattern:
# Stack (LIFO)
# Used when matching pairs and checking correct order.

# Time Complexity:
# O(n)
# Each bracket is pushed and popped at most once.

# Space Complexity:
# O(n)
# In the worst case, all characters are opening brackets and stored in the stack.