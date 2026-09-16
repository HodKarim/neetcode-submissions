class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for i in range(len(operations)):
            if operations[i] == '+':
                res = int(score[-1]) + int(score[-2])
                score.append(str(res))
            elif operations[i] == 'D':
                res = int(score[-1]) * 2
                score.append(str(res))
            elif operations[i] == 'C':
                score.pop()
            else:
                score.append(operations[i])
        sum = 0
        for i in range(len(score)):
            sum += int(score[i])
        return sum
'''
start empty record

x records new score of x

+ records new score sum of prev 2 scores

D records new score double prev score

C invalidates prev score and removes from records

return sum of all scores on records after applying all ops


'''