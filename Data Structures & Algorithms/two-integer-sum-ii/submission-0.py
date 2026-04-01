"""
[1,2,3,4] t = 3
 i j
[1,2]
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [i+1, j+1]
        
        return [-1,-1]