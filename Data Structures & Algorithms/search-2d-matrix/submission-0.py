class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        lo, hi = 0, row*col-1
        while lo < hi:
            mid = (lo+hi)//2
            midVal = matrix[mid//col][mid%col]
            if midVal >= target:
                hi = mid
            else:
                lo = mid+1
        
        return matrix[lo//col][lo%col] == target