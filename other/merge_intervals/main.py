from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            # если текущий интервал начинается не позже конца последнего из списка
            if intervals[i][0] <= merged[-1][1]:
                # последний интервал делаем длинейшим 
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
            else:
                merged.append(intervals[i])
        return merged
