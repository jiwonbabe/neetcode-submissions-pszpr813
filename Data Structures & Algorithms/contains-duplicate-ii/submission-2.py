from collections import defaultdict
class Solution:
    """
    [1,2,3,1] k=2
     i     j
     
     1: [0,3]
     2: [1]
     3: [2]
     Time Complexity: O(n+m*l)
     Space Complexity: O(m)

     1: [0,2,3]
           i j

     0:[1]
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i, n in enumerate(nums):
            if n not in hm:
                hm[n] = i
            else:
                if abs(hm[n]-i) <= k:
                    return True
                else:
                    hm[n] = i
        
        return False


        
