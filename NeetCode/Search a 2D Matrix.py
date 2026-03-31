class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix[0])-1
        row = []

        for arr in matrix:
            if arr[-1] >= target:
                row = arr
                break
        
        while left <= right and row:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right -= 1
            else:
                left += 1

        return False
        
        