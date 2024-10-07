class Solution:
    def is_reflected(self, points) -> bool:
        # отслеживание отклонения x-координат от линии отражения для каждой уникальной y-координаты.
        dct = {}
        # чтобы найти x координату оси
        points.sort()
        if len(points) % 2 == 1:
            # Если количество точек нечетное, линия отражения будет находиться на x-координате средней точки.
            x = points[len(points) // 2][0]
        else:
            # Если количество точек четное, линия будет находиться между двумя центральными точками.
            x = (points[len(points) // 2 - 1][0] + points[len(points) // 2][0]) / 2

        for el in points:
            if el[1] in dct:
                # если y-координата в словаре - прибавляем разницу между x координатой и осью симметрии
                dct[el[1]] += el[0] - x
            else:
                dct[el[1]] = el[0] - x
            # если суммарная разница между x с одинаковыми y = 0 - не учитываем
            if dct[el[1]] == 0:
                dct.pop(el[1])
        # если суммы разных x дают одинаковое значение - то у них разные y
        return len(dct) == 0
