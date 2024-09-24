class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hist = dict()
        max_len, ans, left = 0, 0, 0
        for right in range(len(s)):
            if s[right] in hist:
                hist[s[right]] += 1
            else:
                hist[s[right]] = 1

            max_len = max(max_len, hist[s[right]])
            if right - left + 1 - max_len > k:
                hist[s[left]] -= 1
                left += 1
            ans = max(max_len, right - left + 1)
        return ans
