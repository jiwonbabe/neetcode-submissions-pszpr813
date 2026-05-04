"""
[30,38,30,36,35,40,28]
[(index0,temp0), ]


[1,]
[30,38,30,36,]
[1,1,1]
[75,71,72,]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index = stack[-1][0]
                stack.pop()
                result[index] = i-index
            stack.append((i, temp))
        
        return result
        
