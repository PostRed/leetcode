from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for el in nums:
            # исключающее или
            ans ^= el
        return ans
