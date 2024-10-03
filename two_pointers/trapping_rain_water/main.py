class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        left = 0
        right = len(height) - 1
        max_unit = 0
        while left <= right:
            min_unit = min(height[left], height[right])
            # в максимуме храним максимальный минимум, который мы прошли
            max_unit = max(max_unit, min_unit)
            # правый элемент будет правой границей для воды (не обязательно ближайшей)
            ans += max_unit - min_unit
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
