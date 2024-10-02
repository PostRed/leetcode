class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        # Заполняем результат с конца
        for i in range(n - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            #  Большее из значений записываем в ответ
            if left_square > right_square:
                result[i] = left_square
                left += 1
            else:
                result[i] = right_square
                right -= 1

        return result
