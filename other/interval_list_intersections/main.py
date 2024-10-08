class Solution:
    def intersection(self, i1, i2):
        # большее из начал
        low = max(i1[0], i2[0])
        # меньшее из концов
        high = min(i1[1], i2[1])
        if low > high:
            # это важно, так как до меньшего конца пересечений нет
            return [high]
        return [low, high]

    def intervalIntersection(self, firstList, secondList):
        p1 = p2 = 0
        ans = []
        while p1 < len(firstList) and p2 < len(secondList):
            inter = self.intersection(firstList[p1], secondList[p2])
            if len(inter) > 1:
                ans.append(inter)
            #  Если конец второго больше, чем конец пересечения - сдвигаем указатель в первом
            if secondList[p2][1] > inter[-1]:
                p1 += 1
            #  Если конец второго меньше, чем конец пересечения - сдвигаем указатель во втором
            else:
                p2 += 1
        return ans
