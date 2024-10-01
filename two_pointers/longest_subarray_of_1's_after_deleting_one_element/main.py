class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, zeros, l = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            # сдвигаем окно. пока в нем не будет только один ноль
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            ans = max(ans, r - l - zeros + 1)
        # так как все равно нужно удалить один элемент
        if ans == len(nums):
            return ans - 1
        return ans
