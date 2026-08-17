class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        mid = int(width*height / 2)
        currh = mid // width 
        currw = mid % width
        left = 0
        right = width * height - 1
        if right == 0 and matrix[0][0] == target:
            return True
        while left <= right:
            if matrix[currh][currw] == target:
                return True
            elif matrix[currh][currw] < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = int((right + left) / 2)
            currh = mid // width
            currw = mid % width
        return False