"""
{1:1, 2:2, 3:3} O(n)
(1,1), (2,2), (3,3) O(N)
+ klogU

O(N+ nlogk)
O(n+k)
"""
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        c = Counter(nums)
        for key, cnt in c.items():
            freq[cnt].append(key)

        result = []
        for vals in freq[::-1]:
            for val in vals:
                result.append(val)
                if len(result) == k:
                    return result
        
        return [-1,-1]