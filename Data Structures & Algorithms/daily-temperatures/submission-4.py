class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        mon_stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while mon_stack:
                if temperatures[i] > temperatures[mon_stack[-1]]:
                    result[mon_stack[-1]] = i - mon_stack[-1]
                    mon_stack.pop()
                else:
                    break
            mon_stack.append(i)

        #loop to set everytjing in results to 0
        if mon_stack:
            for i in range(len(mon_stack)):
                result[mon_stack[i]] = 0
        return result
'''
given: array of integers temperatures where each represents the daily temps of the ith day

return retulrs that shows how many days until the warmer (bigger number) appears

[30,38,30,36,35,40,28]

stack (monotonic)

[0]
stack empty. proceed

see 38 index i. if i is bigger than the top of the stack, pop it. keep popping til either empty or its bigger.
after that, append that element to the stack
---------------
mon_stack = [1,2]
result = [1]
--------------



for i in range(len(temperatures)):
    while mon_stack:
        if current index is bigger than the top of the stack
            subtract the current index from top of stack
            pop the top of the stack
        else:
            break
    append the current element
anything left in the stack should be assigned to 0


'''