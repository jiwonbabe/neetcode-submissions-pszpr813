"""
[1,2,4,6] length = 4
prefix = [1,1,2,8]
suffix = [48,24,6,1]

output[i] = prefix[i]*suffix[i]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1 for _ in range(len(nums))]
        suffix_product = [1 for _ in range(len(nums))]

        prefix, suffix = 1, 1
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            prefix_product[i] = prefix

            suffix *= nums[len(nums)-i]
            suffix_product[len(nums)-1-i] = suffix
        
        output = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            output[i] = prefix_product[i]*suffix_product[i]
        
        return output
    


