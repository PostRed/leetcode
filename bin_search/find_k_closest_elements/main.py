class Solution(object):
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - k
        while l < r:
            mid = (l + r) // 2
            print(l, r)
            if abs(arr[mid] - x) > abs(arr[mid + k] - x):
                l = mid + 1
            elif arr[mid] == arr[mid + k] and arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l + k]
