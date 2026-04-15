class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '+-*/' :
                n2 = stack.pop()
                n1 = stack.pop()
                if tokens[i] == '+':
                    result = n1 + n2
                elif tokens[i] == '-':
                    result = n1 - n2
                elif tokens[i] == '*':
                    result = n1 * n2
                elif tokens[i] == '/':
                    result = n1 / n2
                stack.append(int(result))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]

                