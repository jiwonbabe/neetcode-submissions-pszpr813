"""
[1,2,4,6] length = 4
nums =   [1,2,4,6]
prefix = [1,1,2,8]

suffix = [48,24,6,1]

output[i] = prefix[i]*suffix[i]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i]*suffix[i] for i in range(n)]

    


