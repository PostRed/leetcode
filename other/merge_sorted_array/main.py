class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        i1 = m - 1
        i2 = n - 1
        current = m + n - 1
        while i2 >= 0:
            # с конца записываем бОльший из элементов
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[current] = nums1[i1]
                i1 -= 1
            else:
                nums1[current] = nums2[i2]
                i2 -= 1
            current -= 1
