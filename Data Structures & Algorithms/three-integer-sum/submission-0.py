"""
[-1,0,1,2,-1,-4]
1. nums[i] = -1
-nums[i] = nums[j] + nums[k]

output_set = {(nums[i1], nums[j1], nums[k1])}
O(N^2), O(1)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputSet = set()
        for i, num in enumerate(nums):
            seen = set()
            for j in range(i+1, len(nums)):
                diff = nums[i] + nums[j]
                if -diff in seen:
                    outputSet.add(tuple(sorted([nums[i], nums[j], -diff])))
                seen.add(nums[j])
        
        return list(outputSet)