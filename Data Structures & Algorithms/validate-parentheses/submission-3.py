class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
            elif stack and ((stack[-1] == '[' and c == ']') or (stack[-1] == '(' and c == ')') or (stack[-1] == '{' and c == '}')):
                stack.pop()
            else:
                return False
        
        return True if not stack else False