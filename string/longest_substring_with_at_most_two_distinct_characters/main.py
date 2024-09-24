class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        ans = 0
        distincts = 0
        hist = {}
        for right in range(len(s)):
            if s[right] in hist:
                hist[s[right]] += 1
            else:
                hist[s[right]] = 1
                distincts += 1
            # Если в строке больше двух уникальных элементов - сдвигаем левую границу
            if distincts > 2:
                hist[s[left]] -= 1
                if hist[s[left]] == 0:
                    distincts -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
