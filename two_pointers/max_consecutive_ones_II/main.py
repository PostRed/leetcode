class Solution:
    def find_max_consecutive_ones(self, nums):
        ans = 0
        zeros = 0

        l = 0
        for r in range(len(nums)):
            if nums[r]== 0:
                zeros += 1
            while zeros == 2:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
