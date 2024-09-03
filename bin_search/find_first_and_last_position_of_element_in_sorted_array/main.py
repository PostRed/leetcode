class Solution(object):
    def lSearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                res = mid
                r = mid - 1
        return res

    def rSearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        return res

    def searchRange(self, nums, target):
        return [self.lSearch(nums, target), self.rSearch(nums, target)]
