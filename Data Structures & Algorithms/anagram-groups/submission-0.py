from collections import defaultdict
"""
["act","pots","tops","cat","stop","hat"]

1. sorting 
hm[sorted(word)] = [pots, stops, tops]
Time Complexity: O(N*mlogm)
Space Complexity: O(u)

2. without sorting 
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for word in strs:
            hm[tuple(sorted(word))].append(word)
        
        return list(hm.values())