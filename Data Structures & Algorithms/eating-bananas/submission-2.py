"""
[1,4,3,2] h = 9
[1,2,3,4]
(min, max)
min <= k <= max
Time Complexity: O(PlogN)
[4,25]
mid = 14
2+1+2+1
[15,25]
mid=40//2=20
2+1+1+1
[21,25]
mid = 23
2+1+1+
[24,25]
mid=24

"""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h

        lo, hi = 1, piles[0]
        for p in piles:
            lo = min(lo, p)
            hi = max(hi, p)
        
        while lo < hi:
            mid = (lo+hi)//2
            if validate(mid):
                hi = mid
            else:
                lo = mid+1
        
        return lo
            
