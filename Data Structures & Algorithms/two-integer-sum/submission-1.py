"""
1. hashmap
4,5,6  t = 10
    1
{
4: 0,
5: 1
}

2. 

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        
        return [-1,-1]