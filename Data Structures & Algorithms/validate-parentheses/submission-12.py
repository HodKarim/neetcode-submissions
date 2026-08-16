class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        parentheses = {']':'[', '}':'{', ')':'('} 



        for i in range(len(s)):
            if s[i] not in parentheses:
                stack.append(s[i])
            else: #if its the key check if the value is the top of the stack
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if top == parentheses[s[i]]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
        
        '''
        given string w () {} []
        valid if every open bracket is closed w same type of closed bracket


        "([{}])"

        we see ( and add it to the stack since we dont see it in hashmap
        we add [ and add to stack since not in hashmap
        add { since not in hashmap
        see }. its in the hashmap so we dont add to stack. check if corresponding value is top of stack.
        if so, pop it. if not, return false. its in top of stack so pop it
        see ]. pop its value from stack


        '''