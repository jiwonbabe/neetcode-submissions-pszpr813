"""
[1,2,3,4,3]
       i j

i+1
[1,2,3,4]
k = 4

i: track the index of the unique elements
j: traverse whole array to find new unique elements
nums[i] = nums[j]
[2,10,30,30,30,30]
      i.        j 


[2,10,30]
k = 3


"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)

