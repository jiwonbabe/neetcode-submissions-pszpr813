"""
racecar
carrace

1. sorting 
O(nlgn), 
O(1) or O(n)

2. hashmap
O(n)
O(m)


"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        for l in t:
            c[l] -= 1
            if c[l] == 0:
                del c[l]
        
        return True if len(c) == 0 else False
