class Solution:
    def partitionLabels(self, s):
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        left = right = 0
        ans = []
        for i in range(len(s)):
            # правая граница - это самое дальнее вхождение
            right = max(right, last[s[i]])
            # если правее нет, то мы нашли нужный отрезок 
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        return ans
