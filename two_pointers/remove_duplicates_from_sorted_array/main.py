class Solution:
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                # l делаем уникальным элементом
                nums[l] = nums[r]
                l += 1
        # позиция последнего уникального элемента
        return l
