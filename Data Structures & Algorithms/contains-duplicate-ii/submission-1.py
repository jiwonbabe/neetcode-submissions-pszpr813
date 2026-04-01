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
        hm = defaultdict(list)
        for i, n in enumerate(nums):
            hm[n].append(i)
        
        for _, indices in hm.items():
            i, j = 0, len(indices)-1
            while i < len(indices) and j >= 0 and i < j:
                if abs(indices[i]-indices[j]) <= k:
                    return True
                if i+1 >= len(indices):
                    j -= 1
                elif j-1 < 0:
                    i += 1
                elif indices[i+1]-indices[i] > indices[j-1] - indices[j]:
                    i += 1
                else:
                    j -= 1
        
        return False


        
