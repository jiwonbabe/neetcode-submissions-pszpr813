"""
{1:1, 2:2, 3:3} O(n)
(1,1), (2,2), (3,3) O(N)
+ klogU

O(N+klogU)
O(U)
"""
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        maxHeap = []
        for key, cnt in c.items():
            heapq.heappush(maxHeap, (-cnt, key))
        
        results = []
        for _ in range(k):
            (_, key) =  heapq.heappop(maxHeap)
            results.append(key)
        
        return results