class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = 1e9
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                if sum3 > target:
                    k -=1
                else:
                    j += 1
        return res
