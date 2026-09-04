class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','/','*'}

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                if tokens[i] == '+':
                    answer = int(operand1) + int(operand2)
                elif tokens[i] == '-':
                    answer = int(operand1) - int(operand2)
                elif tokens[i] == '*':
                    answer = int(operand1) * int(operand2)
                else:
                    answer = int(operand1 / operand2)
                stack.append(answer)
        return int(stack[-1])
'''
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]




'''