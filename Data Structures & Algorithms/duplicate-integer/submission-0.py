"""
1,2,3,3

{1,2,3,3}
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for n in nums:
            if n in unique:
                return True
            unique.add(n)
        
        return False