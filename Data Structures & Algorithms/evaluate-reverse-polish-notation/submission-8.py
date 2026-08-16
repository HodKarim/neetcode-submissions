class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "/", "*"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == "+":
                    # addition
                    result = int(operand1) + int(operand2)
                elif token == "/":
                    result = int(int(operand1) / int(operand2))
                elif token == "-":
                    result = int(operand1) - int(operand2)
                else:  # token == *
                    result = int(operand1) * int(operand2)
                stack.append(str(result))
        return int(stack[-1])


"""
given: array of strings (tokens) that rep valid arithmetic reverse polish expression

goal: return the result of the expression

["1","2","+","3","*","4","-"]
(((1+2)*3)-4)

[]
when we see an integer, we push into stack
[1]
[1,2]
when we see an operation, we would have 4 options in if statements depending on the 
operator


["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

[10,6,9,3]
see +
pop 3, second operand
pop 9, first operand
9+3 = 12
add 12 to stack:
[10,6,12]
[10,6,12,-11]
oop see another operand!

(9+3)*11)/6)*10)+17)+5)

"""
