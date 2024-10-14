from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        i = 0
        j = 0
        counter = 1
        direction = 0
        while counter <= n * n:
            matrix[i][j] = counter
            # слева на право
            if direction == 0:
                # если столбец последний или дальше уже заполнено - меняем направление
                if j == n - 1 or matrix[i][j + 1] != 0:
                    direction = 1
                    i += 1
                # иначе идем по направлению дальше
                else:
                    j += 1
            # сверху вниз
            elif direction == 1:
                # если последняя строка или дальше уже заполнено - меняем направление
                if i == n - 1 or matrix[i + 1][j] != 0:
                    direction = 2
                    j -= 1
                # иначе идем по направлению дальше
                else:
                    i += 1
            # с права на лево
            elif direction == 2:
                # если первый столбец или дальше уже заполнено - меняем направление
                if j == 0 or matrix[i][j - 1] != 0:
                    direction = 3
                    i -= 1
                # иначе идем по направлению дальше
                else:
                    j -= 1
            # сверху вниз
            else:
                # если первая строка или дальше уже заполнено - меняем направление
                if i == 0 or matrix[i - 1][j] != 0:
                    direction = 0
                    j += 1
                # иначе идем по направлению дальше
                else:
                    i -= 1
            counter += 1
        return matrix

mtr = Solution().generateMatrix(4)
for i in range(4):
    for j in range(4):
        print(mtr[i][j], end=' ')
    print()
