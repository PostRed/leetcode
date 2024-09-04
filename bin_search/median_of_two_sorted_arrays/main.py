class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1 = len(nums1)
        n2 = len(nums2)

        left = 0
        right = n1
        total = n1 + n2
        half_len = (total + 1) // 2

        while left <= right:
            # нужно построить линию так, чтобы все элементы слева были одинаковы и меньше всех (одинаковых) элементов справа
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

            l1 = nums1[mid1 - 1] if mid1 > 0 else -1e9
            r1 = nums1[mid1] if mid1 < n1 else 1e9

            l2 = nums2[mid2 - 1] if mid2 > 0 else -1e9
            r2 = nums2[mid2] if mid2 < n2 else 1e9

            # Если наше условие соблюдено
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)

            elif l1 > r2:
                # то линия левее
                right = mid1 - 1
            else:
                # то линия правее
                left = mid1 + 1
