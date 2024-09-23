class Solution(object):

    def palindrome_expand(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        ans = ''
        for i in range(len(s)):
            # Возвращает палинтромную подстроку нечетной длины
            pal_odd = self.palindrome_expand(i, i, s)
            # Возвращает палинтромную подстроку четной длины
            pal_even =  self.palindrome_expand(i, i + 1, s)
            print(pal_odd)
            ans = max([ans, pal_odd, pal_even], key=len)
        return ans
