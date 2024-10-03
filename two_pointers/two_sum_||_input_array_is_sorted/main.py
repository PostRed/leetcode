class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            # так как список отсортирован, если сумма меньше - ее надо увеличить с помощью передвижения l
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
