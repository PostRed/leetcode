class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        hist = [0] * (cols + 1)  # добавляем один элемент для удобства
        res = 0

        for row in matrix:
            for i in range(len(matrix[0])):
                # Обновляем высоту для текущего столбца
                if row[i] == '1':
                    hist[i] += 1
                else:
                    hist[i] = 0
            # Находим максимальную площадь для текущей "гистограммы"
            res = max(res, self.largestRectangleArea(hist))

        return res

    def largestRectangleArea(self, hist):
        """
        :type hist: List[int]
        :rtype: int
        """
        stack = []
        res = 0

        for i in range(len(hist)):
            # Пока стек не пуст и текущая высота меньше высоты на вершине стека
            while stack and hist[stack[-1]] > hist[i]:
                # Высота прямоугольника равна высоте, соответствующей этому индексу
                h = hist[stack.pop()]

                # Если стек пуст, это означает, что текущая высота является самой низкой до текущего индекса
                if not stack:
                    w = i  # Ширина равна текущему индексу (все столбцы до i)
                else:
                    # Ширина равна разнице между текущим индексом и индексом на вершине стека минус 1
                    w = i - stack[-1] - 1

                res = max(res, h * w)
            stack.append(i)

        return res
