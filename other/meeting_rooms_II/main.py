import heapq

from typing import (
    List,
)


class Solution:

    def min_meeting_rooms_heap(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        heap = []
        for interval in sorted(intervals):
            if len(heap) != 0 and interval[0] >= heap[0]:
                heapq.heappushpop(heap, interval)
            else:
                heapq.heappush(heap, interval)
        return len(heap)

    def min_meeting_rooms_simple(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        intervals.sort()
        rooms = [intervals[0][1]]
        for i in range(1, len(intervals)):
            need_new = True
            if intervals[i][1] >= rooms[-1]:
                    need_new = False
            if need_new:
                rooms.append(intervals[i][1])
        return len(rooms)


