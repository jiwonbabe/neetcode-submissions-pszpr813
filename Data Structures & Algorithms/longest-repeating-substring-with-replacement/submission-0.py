"""
j
i
XYYX
1. 
count[X]=1
length = 1 = j-i+1 - maxf <= k
2. 
count[Y]=1
length = 2 = 2 - 1 <= k
3. 
count[Y]=2
length = 3 = 3 - 2 <= k

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        for i in range(len(s)):
            count = {}
            maxf = -1
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                maxf = max(maxf, count[s[j]])
                if j-i+1 - maxf <= k:
                    length = max(length, j-i+1)
        
        return length
