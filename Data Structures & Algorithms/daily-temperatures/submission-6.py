class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if i == 0:
                mon_stack.append(i)
            else:
                #check if violates rule
                while mon_stack:
                    if temperatures[i] > temperatures[mon_stack[-1]]:
                        top_idx = mon_stack.pop()
                        result[top_idx] = i - top_idx
                    else:
                        break
                mon_stack.append(i)


        return result

'''
given: array of ints (temperatures) where each elem reps the daily temp on that index/day

goal: return array results where each elem is # of days after ith day before a warmer temp
appears on a future day. if none, result[i] = 0





[30,38,30,46,35,40,28]

for every index
'''