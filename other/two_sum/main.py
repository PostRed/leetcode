from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            # если в списке есть число, которое в сумме с текущем даст цель
            if target - nums[i] in indices:
                return [indices[target - nums[i]], i]
            indices[nums[i]] = i
