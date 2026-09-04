class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        mon_stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if mon_stack:
                while mon_stack and temperatures[i] > temperatures[mon_stack[-1]]:
                    top_of_stack = mon_stack.pop()
                    result[top_of_stack] = i - top_of_stack
                mon_stack.append(i)
            else:
                mon_stack.append(i)

        return result
'''
given an array of integers temps where temps[i] is the daily temp on ith day

return array result where result[i] is # of days after ith day before a warmer temp appears

[30,38,30,36,35,40,28]

i = 2

[1,2] 

top_of_stack = 0

[1,0,0,0,0,0,0]


        



'''