class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        # В словарях храним замены букв для каждой из строк
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            if s[i] in dict_s and t[i] != dict_s[s[i]]:
                return False
            elif s[i] not in dict_s and t[i] in dict_t:
                return False
            else:
                dict_s[s[i]] = t[i]
                dict_t[t[i]] = s[i]
        return True
