class Solution(object):
    def summaryRanges(self, nums):
        left = 0
        right = 1
        if len(nums) < 2:
            return list(map(str, nums))
        
        ans = []
        while right < len(nums):
            # упорядоченная последовательность кончилась
            if nums[right - 1] != nums[right] - 1:
                # если только один элемент
                if left == right - 1:
                    ans.append(str(nums[left]))
                else:
                    ans.append(str(nums[left]) + '->' + str(nums[right - 1]))
                # идем искать новое окно
                left = right
                
            right += 1
            
        if left == right - 1:
            ans.append(str(nums[left]))
        else:
            ans.append(str(nums[left]) + '->' + str(nums[right - 1]))
        return ans
