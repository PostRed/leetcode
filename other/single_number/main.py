from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for el in nums:
            # исключающее или, для одинаковых чисел будет давать ноль
            ans ^= el
        return ans
