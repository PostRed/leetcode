from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix) // 2):
            # Отражаем матрицу относительно прямой X (середины)
            matrix[i], matrix[len(matrix) - i - 1] = matrix[len(matrix) - i - 1], matrix[i]
        for i in range(len(matrix)):
            for j in range(i):
                # Отражаем матрицу относительно диагонали
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
