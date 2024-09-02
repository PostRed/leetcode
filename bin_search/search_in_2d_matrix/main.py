class Solution(object):
    def searchMatrix(self, matrix, target):
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            y_mid = mid // len(matrix[0])
            x_mid = mid % len(matrix[0])
            if matrix[y_mid][x_mid] < target:
                l = mid + 1
            elif matrix[y_mid][x_mid] > target:
                r = mid - 1
            else:
                return True
        return False
