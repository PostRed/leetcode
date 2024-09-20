class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_p = len(p)
        len_s = len(s)
        result = []

        if len_p > len_s:
            return result

        p_count = [0] * 26
        s_count = [0] * 26

        # Заполняем массивы для p и первого окна в s
        for i in range(len_p):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        # Сравниваем массивы для первого окна
        if s_count == p_count:
            result.append(0)

        # Перемещаем окно по строке s
        for i in range(len_p, len_s):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - len_p]) - ord('a')] -= 1
            if s_count == p_count:
                result.append(i - len_p + 1)

        return result
